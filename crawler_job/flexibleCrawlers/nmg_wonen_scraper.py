


from typing import Optional
from crawl4ai import AsyncWebCrawler, CrawlResult
from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.models.db_config_models import WebsiteConfig
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class NmgWonenScraper(BaseWebsiteScraper):
    """Nmg Wonen-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
        debug_mode: bool = False,
    ):
        super().__init__(config, session_id, crawler, notification_service, debug_mode)

        logger.info(f"HuisSleutel scraper initialized...")
        
    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.filtering_config:
            logger.info("No filtering configuration provided.")
            return
        logger.info(f"Applying filters to {self.current_url}{self.filtering_config.filter_url_suffix}")
        cookie_config = self.standard_run_config.clone()
        result: CrawlResult = await self.crawler.arun(
            url=f"{self.current_url}{self.filtering_config.filter_url_suffix}", # type: ignore
            config=cookie_config,
        )
        if not result.success:
            raise Exception(f"Failed to apply filters: {result.error_message}")
        
        logger.info("Applied filters")
        self.current_url = result.url