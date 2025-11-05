from typing import Optional
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
)

from crawler_job.helpers.crawler_config_factory import CrawlerConfigFactory
from crawler_job.notifications.notification_service import NotificationService

from ..models.pydantic_models import WebsiteScrapeConfigJson
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger
from crawler_job.helpers.decorators import (
    requires_crawler_initialized,
    requires_login_config,
)

logger = setup_logger(__name__)


class HuisSleutelScraper(BaseWebsiteScraper):
    """Huissleutel-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteScrapeConfigJson,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
    ):
        super().__init__(config, session_id, crawler, notification_service)

        logger.debug("HuisSleutel scraper initialized...")

    @requires_crawler_initialized
    async def navigate_to_gallery_async(self) -> None:
        pass

    def validate_sitemap_data(self):
        pass

    @requires_crawler_initialized
    async def validate_login(self) -> bool:  # type: ignore
        return True

    @requires_crawler_initialized
    async def apply_filters_async(self) -> None:
        pass

    async def login_async(self) -> bool:
        return True

    def get_run_config(self) -> CrawlerRunConfig:
        run_config = super().get_run_config()
        run_config.screenshot = True
        return run_config

    def get_login_run_config(
        self, full_login_url: str, js_code: list[str], wait_for_condition: str
    ) -> CrawlerRunConfig:
        run_config = CrawlerConfigFactory.create_login_run_config(
            self.get_run_config(), full_login_url, js_code, wait_for_condition
        )
        run_config.screenshot = True
        return run_config
