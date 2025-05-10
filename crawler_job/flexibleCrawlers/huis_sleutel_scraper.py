import json
from typing import Dict, Any, List, Optional
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlResult,
    CrawlerMonitor,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
    JsonCssExtractionStrategy,
    PruningContentFilter,
    RateLimiter,
    SemaphoreDispatcher,
)

from crawler_job.models.house_models import FetchedPage, House
from crawler_job.notifications.notification_service import NotificationService

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class HuisSleutelScraper(BaseWebsiteScraper):
    """Huissleutel-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        notification_service: Optional[NotificationService] = None,
        debug_mode: bool = False,
    ):
        super().__init__(config, session_id, notification_service, debug_mode)

        logger.info(f"HuisSleutel scraper initialized...")

    async def navigate_to_gallery_async(self) -> None:
        pass
    
    def validate_sitemap_data(self):
        pass 

    async def validate_login(self) -> bool:  # type: ignore
        pass

    async def validate_login(self) -> bool:  # type: ignore
        return True

    async def apply_filters_async(self) -> None:
        pass

    def _build_crawler(self) -> AsyncWebCrawler:
        self.browser_config = BrowserConfig(
            headless=not self.debug_mode,
            verbose=self.debug_mode,
            use_managed_browser=True,
            user_data_dir="./browser_data/huis_sleutel",
            extra_args=[
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--remote-debugging-address=0.0.0.0",
                "--remote-debugging-port=9222",
            ],
        )

        self.crawler = AsyncWebCrawler(
            config=self.browser_config,
        )

        return self.crawler
