import logging
from typing import Dict, Any
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlResult,
    CrawlerRunConfig,
)

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper

logger = logging.getLogger(__name__)


class VestedaScraper(BaseWebsiteScraper):
    """Vesteda-specific scraper implementation."""

    def __init__(self, config: WebsiteConfig, session_id: str):
        """Initialize the Vesteda scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
        """
        super().__init__(config, session_id)

        logger.info(f"Vesteda scraper initialized...")

    def _build_crawler(self) -> AsyncWebCrawler:
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=True,
            use_managed_browser=True,
            user_data_dir="./browser_data/vesteda",
        )

        self.crawler = AsyncWebCrawler(
            config=self.browser_config,
        )
        
        return self.crawler

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.config.accept_cookies:
            logger.info("Accepting cookies not required/enabled.")
            return True

        if self.accepted_cookies:
            logger.info("Cookies already accepted.")
            return self.accepted_cookies

        logger.info("Accepting cookies...")

        cookie_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            magic=True,
            session_id=self.session_id,
            js_code="""
                (async () => {
                    Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide();
                    const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                    
                    if (cookieButton) {
                        cookieButton.click();
                        console.log("Cookie button clicked");
                    } else {
                        console.log("Cookie button not found");
                        return true;
                    }
                    
                    while (true) {
                        await new Promise(resolve => setTimeout(resolve, 100)); // Wait 100ms
                        const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                        if (cookieButton) {
                            cookieButton.click();
                            console.log("Cookie button clicked");
                            return true;
                        }
                    }
                })();
                """,
        )

        if not self.crawler:
            raise Exception("Crawler not initialized")

        result: CrawlResult = await self.crawler.arun(
            url=current_url, config=cookie_config
        )  # type: ignore

        if not result.success:
            logger.error("Cookie check failed:", result.error_message)
            return False
        elif result.success:
            logger.info(f"Cookies successfully accepted. Current URL: {result.url}")
            self.accepted_cookies = True
            return self.accepted_cookies
        else:
            logger.info("Cookie popup not found or already accepted")
            self.accepted_cookies = True
            return self.accepted_cookies
