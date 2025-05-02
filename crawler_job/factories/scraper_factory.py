from typing import Dict, Type, Optional

from crawl4ai import AsyncWebCrawler

from ..flexibleCrawlers.base_scraper import BaseWebsiteScraper
from ..flexibleCrawlers.vesteda_scraper import VestedaScraper
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)

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
    ):
        """Initialize the scraper factory.

        Args:
            crawler: The crawl4ai crawler instance to use.
            json_config_repo: Repository for new JSON configurations.
        """
        self.crawler = crawler
        self.json_config_repo = json_config_repo

    async def get_scraper_async(self, website_name: str) -> BaseWebsiteScraper:
        """Get a scraper instance for the given website identifier.

        Args:
            identifier: The unique identifier of the website.

        Returns:
            BaseWebsiteScraper: A configured scraper instance.

        Raises:
            ValueError: If no valid configuration is found for the website.
        """
        # Try to get JSON configuration
        website_config = await self.json_config_repo.get_config_by_website_name_async(
            website_name
        )

        if website_config:
            # JSON config found, use corresponding scraper class or crash
            scraper_class = SCRAPER_CLASSES.get(website_name.lower(), BaseWebsiteScraper)
            print(
                f"Using scraper class {scraper_class.__name__} for identifier '{website_name}' with JSON config."
            )
            return scraper_class(crawler=self.crawler, config=website_config)
        else:
            error_msg = (
                f"No valid configuration found for website identifier '{website_name}'."
            )
            print(error_msg)
            raise ValueError(error_msg)
