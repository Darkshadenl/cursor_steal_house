from typing import Dict, Type, Optional

from crawl4ai import AsyncWebCrawler

from crawler_job.crawlers.base_scraper import BaseWebsiteScraper
from ..flexibleCrawlers.vesteda_scraper import VestedaScraper
from crawler_job.services.repositories.json_config_repository import JsonConfigRepository

# Map website identifiers to their specific scraper classes
SCRAPER_CLASSES: Dict[str, Type[BaseWebsiteScraper]] = {
    "vesteda": VestedaScraper,
}


class ScraperFactory:
    """Factory for creating website scrapers with hybrid configuration support."""

    def __init__(
        self,
        crawler: AsyncWebCrawler,
        json_config_repo: JsonConfigRepository,
        old_config_repo: OldConfigRepository,
    ):
        """Initialize the scraper factory.

        Args:
            crawler: The crawl4ai crawler instance to use.
            json_config_repo: Repository for new JSON configurations.
            old_config_repo: Repository for old configuration system.
        """
        self.crawler = crawler
        self.json_config_repo = json_config_repo
        self.old_config_repo = old_config_repo

    async def get_scraper_async(self, identifier: str) -> BaseWebsiteScraper:
        """Get a scraper instance for the given website identifier.

        Args:
            identifier: The unique identifier of the website.

        Returns:
            BaseWebsiteScraper: A configured scraper instance.

        Raises:
            ValueError: If no valid configuration is found for the website.
        """
        # Try to get new JSON configuration
        website_config = await self.json_config_repo.get_config_by_identifier_async(
            identifier
        )

        if website_config:
            # New config found, use corresponding scraper class or fallback to base
            scraper_class = SCRAPER_CLASSES.get(identifier, BaseWebsiteScraper)
            print(
                f"Using scraper class {scraper_class.__name__} for identifier '{identifier}' with JSON config."
            )
            return scraper_class(crawler=self.crawler, config=website_config)
        else:
            # Fallback to old configuration system
            print(
                f"JSON config not found or disabled for '{identifier}'. Attempting fallback to old configuration system."
            )
            old_config = await self.old_config_repo.get_config_async(identifier)

            if old_config:
                # Import old scraper class here to avoid circular imports
                from crawlers.old_system import OldScraperClass

                print(
                    f"Using OLD scraper class OldScraperClass for identifier '{identifier}' with old config system."
                )
                return OldScraperClass(crawler=self.crawler, old_config=old_config)
            else:
                error_msg = f"No valid configuration found for website identifier '{identifier}' in either new JSON system or old system."
                print(error_msg)
                raise ValueError(error_msg)
