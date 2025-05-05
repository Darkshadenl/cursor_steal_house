import logging
from typing import Dict, Any
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

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

        logger.info(f"Vesteda scraper initialized with config: {self.config}")
        
    def _build_crawler(self) -> AsyncWebCrawler:
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=True,
            use_managed_browser=True,
            user_data_dir="./browser_data/vesteda",
        )
        
        self.crawler = AsyncWebCrawler(
            browser_config=self.browser_config,
        )
        return self.crawler
    
