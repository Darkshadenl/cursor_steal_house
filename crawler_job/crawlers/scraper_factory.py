import logging
from typing import Optional

from crawl4ai import AsyncWebCrawler, BrowserConfig
from crawler_job.services.house_service import HouseService
from crawler_job.services.llm_service import LLMService
from crawler_job.services.repositories.config_repository import WebsiteConfigRepository
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.crawlers.base_scraper import AbstractWebsiteScraper
from crawler_job.crawlers.configurable_scraper import ConfigurableWebsiteScraper


logger = logging.getLogger(__name__)


class ScraperFactory:
    """
    Factory for creating website scrapers based on configuration.
    """

    def __init__(
        self,
        config_repository: WebsiteConfigRepository,
        notification_service: Optional[NotificationService] = None,
    ):
        """
        Initialize the scraper factory.

        Args:
            config_repository: Repository for loading website configurations
            notification_service: Optional service for sending notifications
        """
        self.config_repo = config_repository
        self.notification_service = notification_service
        self.logger = logging.getLogger(__name__)

    async def create_scraper_async(self, website_name: str) -> AbstractWebsiteScraper:
        """
        Create a scraper for the specified website.

        Args:
            website_name: Name of the website to create a scraper for

        Returns:
            AbstractWebsiteScraper: Appropriate scraper instance for the website
        """
        try:
            # Get website ID from name
            website_id = await self.config_repo.get_website_id_by_name_async(
                website_name
            )

            # Get browser configuration (could be customized per website in the future)
            browser_config = BrowserConfig(
                headless=True,
                verbose=False,
                use_managed_browser=True,
                user_data_dir=f"./browser_data/{website_name.lower()}",
            )

            # Create services
            crawler = AsyncWebCrawler(config=browser_config)
            house_service = HouseService(notification_service=self.notification_service)
            llm_service = LLMService()

            # Create and return the appropriate scraper
            # Currently only ConfigurableWebsiteScraper is implemented
            # Could be extended to use custom scrapers for specific websites
            scraper = ConfigurableWebsiteScraper(
                crawler=crawler,
                config_repository=self.config_repo,
                house_service=house_service,
                llm_service=llm_service,
                notification_service=self.notification_service,
            )

            self.logger.info(
                f"Created ConfigurableWebsiteScraper for website: {website_name}"
            )
            return scraper

        except Exception as e:
            self.logger.error(
                f"Error creating scraper for website {website_name}: {str(e)}"
            )
            raise

    # Synchronous wrapper for backward compatibility

    def create_scraper(self, website_name: str) -> AbstractWebsiteScraper:
        """
        Synchronous version of create_scraper_async.

        Args:
            website_name: Name of the website to create a scraper for

        Returns:
            AbstractWebsiteScraper: Appropriate scraper instance for the website
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.create_scraper_async(website_name))
        finally:
            loop.close()


__all__ = ["ScraperFactory"]
