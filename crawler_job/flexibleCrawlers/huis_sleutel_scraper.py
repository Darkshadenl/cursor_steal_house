from typing import Optional
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    SemaphoreDispatcher,
)

from crawler_job.helpers.crawler_config_factory import CrawlerRunConfigFactory
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.data_processing_service import DataProcessingService
from crawler_job.services.llm_extraction_service import LlmExtractionService
from crawler_job.helpers.config_validator import WebsiteConfigValidator

from ..models.pydantic_models import WebsiteScrapeConfigJson
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger
from crawler_job.helpers.decorators import (
    requires_crawler_initialized,
)

logger = setup_logger(__name__)


class HuisSleutelScraper(BaseWebsiteScraper):
    """Huissleutel-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteScrapeConfigJson,
        session_id: str,
        crawler: AsyncWebCrawler,
        standard_run_config: CrawlerRunConfig,
        standard_dispatcher: SemaphoreDispatcher,
        data_processing_service: DataProcessingService,
        llm_extraction_service: LlmExtractionService,
        config_validator: WebsiteConfigValidator,
        notification_service: Optional[NotificationService] = None,
    ):
        super().__init__(
            config=config,
            session_id=session_id,
            crawler=crawler,
            standard_run_config=standard_run_config,
            standard_dispatcher=standard_dispatcher,
            data_processing_service=data_processing_service,
            llm_extraction_service=llm_extraction_service,
            config_validator=config_validator,
            notification_service=notification_service,
        )

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
        run_config = self.get_run_config()
        run_config.js_code = js_code
        run_config.wait_for = wait_for_condition
        run_config.page_timeout = 10000
        return run_config
