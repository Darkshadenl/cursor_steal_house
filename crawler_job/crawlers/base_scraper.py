from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Tuple

from crawler_job.models.house_models import House
from crawler_job.models.db_config_models import WebsiteConfig
from crawler_job.services.repositories.config_repository import WebsiteConfigRepository


class AbstractWebsiteScraper(ABC):
    """
    Abstract base class for website scrapers.
    Defines the interface that all concrete scraper implementations must follow.
    """

    @abstractmethod
    async def load_config_async(self, website_id: int) -> None:
        """
        Load the website configuration from the database.

        Args:
            website_id: ID of the website to load configuration for
        """
        pass

    @abstractmethod
    async def login_async(self) -> bool:
        """
        Log in to the website if required.

        Returns:
            bool: True if login was successful or not needed, False otherwise
        """
        pass

    @abstractmethod
    async def navigate_to_gallery_async(self) -> str:
        """
        Navigate to the gallery/search page with all property listings.

        Returns:
            str: URL of the gallery page
        """
        pass

    @abstractmethod
    async def extract_gallery_async(self) -> List[House]:
        """
        Extract property listings from the gallery/search results page.

        Returns:
            List[House]: List of extracted house objects with basic information
        """
        pass

    @abstractmethod
    async def extract_details_async(self, gallery_item: House) -> Optional[House]:
        """
        Extract detailed information for a specific property.

        Args:
            gallery_item: House object with basic information from the gallery

        Returns:
            Optional[House]: Complete House object with all available details, or None if extraction failed
        """
        pass

    @abstractmethod
    async def run_async(self, website_id: int) -> Dict[str, Any]:
        """
        Run the complete scraping process.

        Args:
            website_id: ID of the website to scrape

        Returns:
            Dict[str, Any]: Results of the scraping process
        """
        pass

    # Synchronous wrapper methods for backward compatibility

    def load_config(self, website_id: int) -> None:
        """
        Synchronous wrapper for load_config_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.load_config_async(website_id))
        finally:
            loop.close()

    def login(self) -> bool:
        """
        Synchronous wrapper for login_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.login_async())
        finally:
            loop.close()

    def navigate_to_gallery(self) -> str:
        """
        Synchronous wrapper for navigate_to_gallery_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.navigate_to_gallery_async())
        finally:
            loop.close()

    def extract_gallery(self) -> List[House]:
        """
        Synchronous wrapper for extract_gallery_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.extract_gallery_async())
        finally:
            loop.close()

    def extract_details(self, gallery_item: House) -> Optional[House]:
        """
        Synchronous wrapper for extract_details_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.extract_details_async(gallery_item))
        finally:
            loop.close()

    def run(self, website_id: int) -> Dict[str, Any]:
        """
        Synchronous wrapper for run_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.run_async(website_id))
        finally:
            loop.close()


__all__ = ["AbstractWebsiteScraper"]
