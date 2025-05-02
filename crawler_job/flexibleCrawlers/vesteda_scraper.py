import logging
from typing import Dict, Any
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper

logger = logging.getLogger(__name__)


class VestedaScraper(BaseWebsiteScraper):
    """Vesteda-specific scraper implementation."""

    def __init__(self, crawler: AsyncWebCrawler, config: WebsiteConfig):
        """Initialize the Vesteda scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
        """
        super().__init__(crawler, config)

        logger.info(f"Vesteda scraper initialized with config: {self.config}")
        self.detail_config: CrawlerRunConfig = self.standard_run_config()

    async def extract_details_async(self, url: str) -> Dict[str, Any]:
        """Override detail extraction for Vesteda-specific optimizations.

        Args:
            url: The URL of the detail page to scrape.

        Returns:
            Dict[str, Any]: The extracted data.
        """
        # Use Vesteda-specific configuration for detail pages
        await self.crawler.goto(url, config=self.detail_config)

        # Wait for critical content to load
        await self.crawler.wait_for_selector(
            ".property-details-container", config=self.detail_config
        )

        result = {}

        # Extract fields with custom error handling
        for field in self.config.strategy_config.detail_page_extraction_config.fields:
            try:
                # Wait for each field to be available
                element = await self.crawler.wait_for_selector(
                    field.selector, config=self.detail_config
                )

                if not element:
                    if field.is_required:
                        print(
                            f"Required field '{field.target_field}' not found on Vesteda detail page"
                        )
                    continue

                if field.extraction_type == "text":
                    value = await element.text()
                elif field.extraction_type == "html":
                    value = await element.inner_html()
                elif field.extraction_type == "attribute" and field.attribute_name:
                    value = await element.get_attribute(field.attribute_name)

                # Apply Vesteda-specific transformations if needed
                if field.transformation_rule and value:
                    # Implement custom transformations here
                    pass

                result[field.target_field] = value

            except Exception as e:
                print(
                    f"Error extracting Vesteda field '{field.target_field}': {str(e)}"
                )
                if field.is_required:
                    break

        return result
