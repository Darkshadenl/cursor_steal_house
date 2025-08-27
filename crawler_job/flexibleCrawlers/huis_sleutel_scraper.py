from typing import Optional
from crawl4ai import (
    AsyncWebCrawler,
)

from crawler_job.notifications.notification_service import NotificationService

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger
from crawler_job.helpers.decorators import requires_crawler_initialized

logger = setup_logger(__name__)


class HuisSleutelScraper(BaseWebsiteScraper):
    """Huissleutel-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
        debug_mode: bool = False,
    ):
        super().__init__(config, session_id, crawler, notification_service, debug_mode)

        logger.info("HuisSleutel scraper initialized...")

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
