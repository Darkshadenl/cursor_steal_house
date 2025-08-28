from typing import Dict, Optional, Type

from crawl4ai import AsyncWebCrawler

from crawler_job.flexibleCrawlers.huis_sleutel_scraper import HuisSleutelScraper
from crawler_job.flexibleCrawlers.nmg_wonen_scraper import NmgWonenScraper
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger

from ..flexibleCrawlers.base_scraper import BaseWebsiteScraper
from ..flexibleCrawlers.vesteda_scraper import VestedaScraper
from ..flexibleCrawlers.huis_sleutel_scraper import HuisSleutelScraper
from ..flexibleCrawlers.nmg_wonen_scraper import NmgWonenScraper
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
            return scraper_class(
                config=website_config,
                session_id=website_config.session_id,
                crawler=self.crawler,
                notification_service=notification_service,
            )
        else:
            error_msg = (
                f"No valid configuration found for website identifier '{website_name}'."
            )
            self.logger.error(error_msg)
            raise ValueError(error_msg)
