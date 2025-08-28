from typing import Dict, Any

from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.services.llm_service import LLMProvider
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class StrategyExecutor:
    def __init__(self, scraper: BaseWebsiteScraper):
        self.scraper = scraper

    async def run_scraper(self) -> Dict[str, Any]:
        from crawler_job.flexibleCrawlers.base_scraper import ScrapeStrategy

        strategy = self.scraper.website_config.scrape_strategy
        logger.info(
            f"Choosing strategy {strategy} for {self.scraper.website_info.name}"
        )
        if strategy == ScrapeStrategy.GALLERY.value:
            result = await self._run_gallery_scrape()
        elif strategy == ScrapeStrategy.SITEMAP.value:
            result = await self._run_sitemap_scrape()
        else:
            raise Exception(f"Invalid scrape strategy: {strategy}")

        return result

    async def _run_gallery_scrape(self) -> Dict[str, Any]:
        await self.scraper.navigate_to_gallery_async()
        await self.scraper.login_async()
        await self.scraper.navigate_to_gallery_async(force_navigation=True)
        await self.scraper.apply_filters_async()
        houses = await self.scraper.extract_gallery_async()
        new_houses = await self.scraper.data_processing_service.check_if_houses_exist(
            houses
        )

        if not new_houses or len(new_houses) == 0:
            self.scraper.logger.info("No new houses found, we're done here!")
            self.scraper.default_results["success"] = True
            return self.scraper.default_results

        detailed_houses = []
        if self.scraper.detail_page_extraction_config.schema_type in ["xpath", "css"]:
            detailed_houses = await self.scraper.process_details_xpath_css(new_houses)
        elif self.scraper.detail_page_extraction_config.schema_type == "llm":
            fetched_pages = await self.scraper.extract_fetched_pages_async(new_houses)
            detailed_houses = (
                await self.scraper.llm_extraction_service.execute_llm_extraction(
                    fetched_pages, provider=LLMProvider.GEMINI
                )
            )

        if not detailed_houses:
            self.scraper.logger.info("No detailed houses found. Exiting...")
            self.scraper.default_results["success"] = True
            return self.scraper.default_results

        self.scraper.data_processing_service.merge_detailed_houses(
            houses, detailed_houses
        )

        await self.scraper.data_processing_service.store_houses(houses)

        return {
            "success": True,
            "total_houses_count": len(houses),
            "new_houses_count": len(new_houses),
            "updated_houses_count": len(houses) - len(new_houses),
        }

    async def _run_sitemap_scrape(self) -> Dict[str, Any]:
        await self.scraper.login_async()

        # if not await self.scraper.validate_login():
        #     self.scraper.logger.error("Login failed, aborting scrape")
        #     return self.scraper.default_results

        sitemap_html = await self.scraper.navigate_to_sitemap_async()
        await self.scraper.apply_filters_async()
        houses = await self.scraper.extract_sitemap_async(sitemap_html)
        new_houses = await self.scraper.data_processing_service.check_if_houses_exist(
            houses
        )
        await self.scraper.data_processing_service.store_houses(new_houses)

        return {
            "success": True,
            "total_houses_count": len(houses),
            "new_houses_count": len(new_houses),
            "updated_houses_count": len(houses) - len(new_houses),
        }
