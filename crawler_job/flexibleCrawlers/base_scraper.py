import json
import logging
from typing import Dict, Any, List, Optional
import os
from abc import ABC, abstractmethod
import asyncio

from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlResult,
    CrawlerRunConfig,
)
from crawler_job.models.db_config_models import WebsiteConfig
from crawler_job.models.house_models import House, FetchedPage
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.house_service import HouseService
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class BaseWebsiteScraper(ABC):
    """Base class for website scrapers using the hybrid configuration system."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        notification_service: Optional[NotificationService] = None,
    ):
        """Initialize the scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
            notification_service: The notification service to use.
        """
        self.config = config
        self.notification_service = notification_service

        if self.config.strategy_config.login_config:
            self.login_config = self.config.strategy_config.login_config

        self.session_id = session_id
        self.standard_run_config = self._build_standard_run_config()
        self.crawler: Optional[AsyncWebCrawler] = None
        self.accepted_cookies = False
        self.navigated_to_gallery = False
        self.current_url = ""
        self.default_results = {
            "success": False,
            "total_houses_count": 0,
            "new_houses_count": 0,
            "updated_houses_count": 0,
        }

    async def validate_current_page(self, expected_url: str, check_url: str) -> bool:
        """Validate if the current page is the expected page.

        Args:
            expected_url: The expected URL to validate against.

        Returns:
            bool: True if the current page is the expected page, False otherwise.
        """
        if not self.crawler:
            raise Exception("Crawler not initialized")

        check_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            js_only=False,
            magic=False,
            user_agent_mode="random",
        )

        logger.info(f"Verifying... Expected URL: {expected_url}")

        check_result: CrawlResult = await self.crawler.arun(
            url=check_url, config=check_config
        )  # type: ignore

        if not check_result.success:
            raise Exception(f"Check verification failed: {check_result.error_message}")

        # logger.debug(f"Check result: {check_result}")

        if (
            check_result.url != expected_url
            and check_result.redirected_url != expected_url
        ):
            raise Exception(f"Verification failed: We're not on the expected page")

        return True

    def _build_standard_run_config(self) -> CrawlerRunConfig:
        """Build the standard crawler run configuration.

        Returns:
            CrawlerRunConfig: The default configuration for crawl4ai.
        """
        return CrawlerRunConfig(
            log_console=True,
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            js_only=False,
            magic=False,
            user_agent_mode="random",
        )

    async def login_async(self) -> bool:
        """Perform login if login configuration is provided.

        Returns:
            bool: True if login was successful or not required, False if login failed.
        """
        if not self.login_config or self.navigated_to_gallery:
            return True

        if not self.crawler:
            raise Exception("Crawler not initialized")

        if not self.accepted_cookies:
            await self._accept_cookies(self.current_url)  # type: ignore

        try:
            base_url = self.config.base_url
            login_url = self.login_config.login_url_path

            full_login_url = f"{base_url}{login_url}"
            logger.info(
                f"Navigating to login page of {self.config.website_name} and logging in.\nUrl: {full_login_url}"
            )
            email = os.getenv(self.config.website_identifier.upper() + "_EMAIL")
            password = os.getenv(self.config.website_identifier.upper() + "_PASSWORD")

            js_code = [
                f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.login_config.submit_selector}').click();",
            ]

            run_config = CrawlerRunConfig(
                session_id=self.session_id,
                exclude_all_images=True,
                exclude_social_media_links=True,
                cache_mode=CacheMode.BYPASS,
                js_only=False,
                magic=False,
                js_code=js_code,
            )

            # logger.debug(f"Run config: {run_config}")
            # logger.debug(f"JS code: {js_code}")

            login_result: CrawlResult = await self.crawler.arun(
                full_login_url, config=run_config
            )  # type: ignore

            if not login_result.success:
                raise Exception(
                    f"Login form submission failed: {login_result.error_message}"
                )
            # logger.debug(f"Login result: {login_result}")
            await asyncio.sleep(2)
            logger.info(f"Validating login success of {self.config.website_name}")

            valid: bool = await self.validate_current_page(
                self.login_config.expected_url,
                f"{self.config.base_url}{self.login_config.success_check_url_path}",
            )
            self.current_url = self.login_config.expected_url

            return valid

        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    async def navigate_to_gallery_async(self) -> None:
        """Navigate to the listings/gallery page."""
        if self.navigated_to_gallery:
            return

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info(f"Navigating to gallery...")
        url = f"{self.config.base_url}{self.config.strategy_config.navigation_config.listings_page_url}"

        result: CrawlResult = await self.crawler.arun(
            url,
            config=self.standard_run_config,
        )  # type: ignore

        full_login_url = f"{self.config.base_url}{self.login_config.login_url_path}"

        if result and result.success and result.redirected_url != full_login_url:
            logger.info(f"Navigating to gallery successful: {result.url}")
            self.navigated_to_gallery = True
            self.current_url = result.url
        else:
            self.current_url = result.redirected_url
            logger.error(f"Navigating to gallery failed: {result.error_message}")
            logger.error(f"Redirected URL: {result.redirected_url}")

    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.config.strategy_config.filtering_config:
            logger.info("No filtering configuration provided.")
            return

        logger.error("Implementing filtering configuration in derived class!")
        raise NotImplementedError(
            "Implementing filtering configuration in derived class!"
        )

    async def extract_gallery_async(self) -> List[House]:
        """Extract data from the gallery/listings page.

        Returns:
            List[House]: Extracted data for each listing item.
        """
        if not self.config.strategy_config.gallery_extraction_config:
            logger.info("No gallery extraction configuration provided.")
            raise Exception("No gallery extraction configuration provided.")

        logger.error("Implementing gallery extraction configuration in derived class!")
        raise NotImplementedError(
            "Implementing gallery extraction configuration in derived class!"
        )

    async def extract_details_async(self, houses: List[House]) -> List[FetchedPage]:
        """Extract data from a detail page.

        Args:
            houses: The list of houses to scrape.

        Returns:
            List[FetchedPage]: The list of fetched pages.
        """
        if not self.config.strategy_config.detail_page_extraction_config:
            raise Exception("No detail page extraction configuration provided.")

        raise NotImplementedError(
            "Implementing detail page extraction configuration in derived class!"
        )

    @abstractmethod
    def _build_crawler(self) -> AsyncWebCrawler:
        pass

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.config.accept_cookies:
            logger.info("Accepting cookies not required/enabled.")
            return True
        return False

    async def _check_if_houses_exist(self, houses: List[House]) -> List[House]:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            new_houses = await house_service.identify_new_houses_async(houses)

            if not new_houses:
                return []

            logger.info(f"Fetching details for {len(new_houses)} new houses...")
            return new_houses

    def _merge_detailed_houses(
        self, houses: List[House], detailed_houses: List[House]
    ) -> None:
        for detailed_house in detailed_houses:
            for house in houses:
                if (
                    house.address == detailed_house.address
                    and house.city == detailed_house.city
                ):
                    for field, value in detailed_house.model_dump(
                        exclude_unset=True
                    ).items():
                        if value is not None and (
                            getattr(house, field) is None
                            or field not in ["address", "city", "status"]
                        ):
                            setattr(house, field, value)
                    break

    async def _store_houses(self, houses: List[House]) -> None:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            await house_service.store_houses_atomic_async(
                houses=houses,
            )

    async def execute_llm_extraction(
        self, fetched_pages: List[FetchedPage], provider: LLMProvider
    ) -> List[House]:
        """
        Extract structured data from markdown using LLM

        Args:
            fetched_pages: List of fetched detail pages
            provider: LLM provider to use

        Returns:
            List[House]: List of House objects with extracted data
        """
        llm_service = LLMService()
        schema = House.model_json_schema()
        houses: List[House] = []

        logger.info("Extracting structured data using LLM...")

        for page in fetched_pages:
            if not page.success:
                continue

            try:
                extracted_data: Optional[Dict[str, Any]] = await llm_service.extract(
                    page.markdown, schema, provider
                )

                if extracted_data is None:
                    logger.warning(f"No data extracted for {page.url}")
                    continue

                json_data = json.loads(extracted_data)  # type: ignore
                house = House.from_dict(json_data)
                houses.append(house)
                logger.info(f"Successfully extracted data for {page.url}")
            except Exception as e:
                logger.warning(f"Error extracting data for {page.url}: {str(e)}")
                continue

        return houses

    async def run_async(self) -> Dict[str, Any]:
        """Run the complete scraping process.

        Returns:
            List[Dict[str, Any]]: The collected data from all listings.
        """
        logger.info(f"Building crawler...")
        self.crawler = self._build_crawler()

        try:
            logger.info(f"Starting crawler...")
            await self.crawler.start()

            await self.navigate_to_gallery_async()

            if not await self.login_async():
                logger.error("Login failed, aborting scrape")
                return self.default_results

            await self.navigate_to_gallery_async()

            await self.apply_filters_async()
            houses = await self.extract_gallery_async()
            new_houses = await self._check_if_houses_exist(houses)

            if not new_houses or len(new_houses) == 0:
                logger.info("No new houses found, we're done here!")
                self.default_results["success"] = True
                return self.default_results

            fetched_pages = await self.extract_details_async(new_houses)
            detailed_houses = await self.execute_llm_extraction(
                fetched_pages, provider=LLMProvider.GEMINI
            )

            if not detailed_houses:
                logger.info("No detailed houses found. Exiting...")
                self.default_results["success"] = True
                return self.default_results

            self._merge_detailed_houses(houses, detailed_houses)

            await self._store_houses(houses)

            return {
                "success": True,
                "total_houses_count": len(houses),
                "new_houses_count": len(new_houses),
                "updated_houses_count": len(houses) - len(new_houses),
            }
        except Exception as e:
            logger.error(f"Error during scraping: {e}")
            while True:
                # wait for 10 seconds
                await asyncio.sleep(10)
            raise e
        finally:
            await self.crawler.close()
