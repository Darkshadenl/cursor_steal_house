from typing import Dict, Optional, Type

from crawl4ai import AsyncWebCrawler

from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.flexibleCrawlers.huis_sleutel_scraper import HuisSleutelScraper
from crawler_job.flexibleCrawlers.nmg_wonen_scraper import NmgWonenScraper
from crawler_job.flexibleCrawlers.vesteda_scraper import VestedaScraper
from crawler_job.helpers.config_validator import WebsiteConfigValidator
from crawler_job.helpers.crawler_config_factory import CrawlerRunConfigFactory
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services import config as global_config
from crawler_job.services.data_processing_service import DataProcessingService
from crawler_job.services.llm_extraction_service import LlmExtractionService
from crawler_job.services.logger_service import setup_logger
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)

SCRAPER_CLASSES: Dict[str, Type[BaseWebsiteScraper]] = {
    "vesteda": VestedaScraper,
    "de_huis_sleutel": HuisSleutelScraper,
    "nmg_wonen": NmgWonenScraper,
}


class ScraperFactory:

    def __init__(
        self,
        json_config_repo: JsonConfigRepository,
        crawler: AsyncWebCrawler,
    ):
        self.json_config_repo = json_config_repo
        self.logger = setup_logger(__name__)
        self.crawler = crawler

    async def get_scraper_async(
        self,
        website_name: str,
        notification_service: Optional[NotificationService] = None,
    ) -> BaseWebsiteScraper:
        website_config = await self.json_config_repo.get_config_by_website_name_async(
            website_name
        )

        if website_config:
            scraper_class = SCRAPER_CLASSES.get(
                website_name.lower(), BaseWebsiteScraper
            )
            self.logger.info(
                f"Using scraper class {scraper_class.__name__} for identifier '{website_config.website_name}' with JSON config."
            )
            if notification_service is None:
                raise ValueError(
                    "Notification service is required to initialize a scraper."
                )
            standard_run_config = CrawlerRunConfigFactory.create_standard_run_config(
                website_config.session_id, global_config.debug_mode
            )
            standard_dispatcher = CrawlerRunConfigFactory.create_standard_dispatcher()
            data_processing_service = DataProcessingService(notification_service)
            llm_extraction_service = LlmExtractionService()
            config_validator = WebsiteConfigValidator(website_config)
            return scraper_class(
                config=website_config,
                session_id=website_config.session_id,
                crawler=self.crawler,
                standard_run_config=standard_run_config,
                standard_dispatcher=standard_dispatcher,
                data_processing_service=data_processing_service,
                llm_extraction_service=llm_extraction_service,
                config_validator=config_validator,
                notification_service=notification_service,
            )
        else:
            error_msg = (
                f"No valid configuration found for website identifier '{website_name}'."
            )
            self.logger.error(error_msg)
            raise ValueError(error_msg)
