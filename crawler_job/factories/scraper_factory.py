from typing import Dict, Optional, Type

from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger

from ..flexibleCrawlers.base_scraper import BaseWebsiteScraper
from ..flexibleCrawlers.vesteda_scraper import VestedaScraper
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)

# Map website identifiers to their specific scraper classes
SCRAPER_CLASSES: Dict[str, Type[BaseWebsiteScraper]] = {
    "vesteda": VestedaScraper,
}

logger = setup_logger(__name__)

class ScraperFactory:
    """Factory for creating website scrapers with hybrid configuration support."""

    def __init__(
        self,
        json_config_repo: JsonConfigRepository,
    ):
        """Initialize the scraper factory.

        Args:
            crawler: The crawl4ai crawler instance to use.
            json_config_repo: Repository for new JSON configurations.
        """
        self.json_config_repo = json_config_repo

    async def get_scraper_async(self, website_name: str, notification_service: Optional[NotificationService] = None) -> BaseWebsiteScraper:
        """Get a scraper instance for the given website identifier.

        Args:
            identifier: The unique identifier of the website.
            notification_service: The notification service to use.
        Returns:
            BaseWebsiteScraper: A configured scraper instance.

        Raises:
            ValueError: If no valid configuration is found for the website.
        """
        website_config = await self.json_config_repo.get_config_by_website_name_async(
            website_name
        )

        if website_config:
            scraper_class = SCRAPER_CLASSES.get(
                website_name.lower(), BaseWebsiteScraper
            )
            logger.info(
                f"Using scraper class {scraper_class.__name__} for identifier '{website_name}' with JSON config."
            )
            return scraper_class(
                config=website_config,
                session_id=website_config.session_id,
                notification_service=notification_service,
            )   
        else:
            error_msg = (
                f"No valid configuration found for website identifier '{website_name}'."
            )
            logger.error(error_msg)
            raise ValueError(error_msg)
