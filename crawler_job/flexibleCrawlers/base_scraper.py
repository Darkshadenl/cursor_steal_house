import logging
from typing import Dict, Any, AsyncGenerator, List, Optional
import os
from abc import ABC, abstractmethod
import asyncio

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlResult,
    CrawlerRunConfig,
)
from crawler_job.models.db_config_models import WebsiteConfig

logger = logging.getLogger(__name__)


class BaseWebsiteScraper(ABC):
    """Base class for website scrapers using the hybrid configuration system."""

    def __init__(self, config: WebsiteConfig, session_id: str):
        """Initialize the scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
        """
        self.config = config

        if self.config.strategy_config.login_config:
            self.login_config = self.config.strategy_config.login_config

        self.session_id = session_id
        self.standard_run_config = self._build_standard_run_config()
        self.crawler: Optional[AsyncWebCrawler] = None
        self.accepted_cookies = False
        self.navigated_to_gallery = False
        self.current_url = ""

    async def validate_current_page(self, expected_url: str, check_url: str) -> bool:
        """Validate if the current page is the expected page.

        Args:
            expected_url: The expected URL to validate against.

        Returns:
            bool: True if the current page is the expected page, False otherwise.
        """
        check_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        )

        await asyncio.sleep(1)
        logger.info(f"Verifying... Expected URL: {expected_url}")

        if not self.crawler:
            raise Exception("Crawler not initialized")

        check_result: CrawlResult = await self.crawler.arun(
            url=check_url, config=check_config
        )  # type: ignore

        if not check_result.success:
            raise Exception(f"Check verification failed: {check_result.error_message}")

        if (
            check_result.url != expected_url
            and check_result.redirected_url != expected_url
        ):
            raise Exception(f"Veficitation failed: We're not on the expected page")

        return True

    def _build_standard_run_config(self) -> CrawlerRunConfig:
        """Build the standard crawler run configuration.

        Returns:
            CrawlerRunConfig: The default configuration for crawl4ai.
        """
        return CrawlerRunConfig(
            log_console=False,
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            js_only=False,
            magic=True,
            user_agent_mode="random",
        )

    async def login_async(self) -> bool:
        """Perform login if login configuration is provided.

        Returns:
            bool: True if login was successful or not required, False if login failed.
        """
        if not self.login_config or self.navigated_to_gallery:
            return True

        if not self.crawler:
            raise Exception("Crawler not initialized")

        try:
            base_url = self.config.base_url
            login_url = self.login_config.login_url_path

            full_login_url = f"{base_url}{login_url}"
            email = os.getenv(self.config.website_identifier.upper() + "_EMAIL")
            password = os.getenv(self.config.website_identifier.upper() + "_PASSWORD")

            run_config = CrawlerRunConfig(
                session_id=self.session_id,
                cache_mode=CacheMode.BYPASS,
                js_only=True,
                magic=True,
                js_code=[
                    f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                    f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                    f"document.querySelector('{self.login_config.submit_selector}').click();",
                ],
            )

            logger.info(
                f"Navigating to login page of {self.config.website_name} and logging in.\nUrl: {full_login_url}"
            )

            login_result: CrawlResult = await self.crawler.arun(
                full_login_url, config=run_config
            )  # type: ignore

            if not login_result.success:
                raise Exception(
                    f"Login form submission failed: {login_result.error_message}"
                )

            valid: bool = await self.validate_current_page(
                self.login_config.expected_url, self.login_config.success_check_url
            )
            if valid:
                await self._accept_cookies(self.current_url)

            return login_result.success

        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    async def navigate_to_gallery_async(self) -> None:
        """Navigate to the listings/gallery page."""
        if self.navigated_to_gallery:
            return

        if not self.crawler:
            raise Exception("Crawler not initialized")

        result: CrawlResult = await self.crawler.arun(
            self.config.strategy_config.navigation_config.listings_page_url,
            config=self.standard_run_config,
        )  # type: ignore

        full_login_url = f"{self.config.base_url}{self.login_config.login_url_path}"

        if result and result.success and result.redirected_url != full_login_url:
            logger.info(f"Search navigation successful: {result.url}")
            self.navigated_to_gallery = True
        else:
            logger.error(f"Search navigation failed: {result.error_message}")
            logger.error(f"Redirected URL: {result.redirected_url}")

    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.config.strategy_config.filtering_config:
            logger.info("No filtering configuration provided.")
            return
        
        logger.error("Implementing filtering configuration in derived class!")
        raise NotImplementedError("Implementing filtering configuration in derived class!")

    async def extract_gallery_async(self) -> AsyncGenerator[Dict[str, Any], None]:
        """Extract data from the gallery/listings page.

        Yields:
            Dict[str, Any]: Extracted data for each listing item.
        """
        if not self.config.strategy_config.gallery_extraction_config:
            logger.info("No gallery extraction configuration provided.")
            raise Exception("No gallery extraction configuration provided.")
        
        logger.error("Implementing gallery extraction configuration in derived class!")
        raise NotImplementedError("Implementing gallery extraction configuration in derived class!")

    async def extract_details_async(self, url: str) -> Dict[str, Any]:
        """Extract data from a detail page.

        Args:
            url: The URL of the detail page to scrape.

        Returns:
            Dict[str, Any]: The extracted data.
        """
        if not self.config.strategy_config.detail_page_extraction_config:
            raise Exception("No detail page extraction configuration provided.")
        
        logger.error("Implementing detail page extraction configuration in derived class!")
        raise NotImplementedError("Implementing detail page extraction configuration in derived class!")

    @abstractmethod
    def _build_crawler(self) -> AsyncWebCrawler:
        pass

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.config.accept_cookies:
            logger.info("Accepting cookies not required/enabled.")
            return True
        return False

    async def run_async(self) -> List[Dict[str, Any]]:
        """Run the complete scraping process.

        Returns:
            List[Dict[str, Any]]: The collected data from all listings.
        """
        results = []

        self.crawler = self._build_crawler()

        await self.crawler.awarmup()
        await self.crawler.start()

        await self.navigate_to_gallery_async()

        if not await self.login_async():
            logger.error("Login failed, aborting scrape")
            return results

        await self.navigate_to_gallery_async()

        await self.apply_filters_async()

        async for item in await self.extract_gallery_async():
            if "url" in item:
                details = await self.extract_details_async(item["url"])
                results.append({**item, **details})
            else:
                results.append(item)

        await self.crawler.close()

        return results
