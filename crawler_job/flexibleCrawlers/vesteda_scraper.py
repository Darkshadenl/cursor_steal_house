from typing import Dict, Any
from crawl4ai import AsyncWebCrawler

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper

class VestedaScraper(BaseWebsiteScraper):
    """Vesteda-specific scraper implementation."""

    def __init__(self, crawler: AsyncWebCrawler, config: WebsiteConfig):
        """Initialize the Vesteda scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
        """
        super().__init__(crawler, config)

        # Vesteda-specific run configurations
        self.filter_config = self.standard_run_config.model_copy(
            update={
                "wait_for_navigation": "networkidle0",  # Wait for all network requests to finish
                "default_timeout_ms": 60000,  # Longer timeout for filter operations
            }
        )

        self.detail_config = self.standard_run_config.model_copy(
            update={
                "block_resources": {
                    "types": [
                        "image",
                        "font",
                        "media",
                        "stylesheet",
                    ],  # Block more resources for detail pages
                    "patterns": [
                        "*.google-analytics.com",
                        "*.doubleclick.net",
                    ],  # Block tracking
                }
            }
        )

    async def apply_filters_async(self) -> None:
        """Override filter application for Vesteda-specific behavior."""
        if not self.config.strategy_config.filtering_config:
            return

        # Wait for filter container to be ready
        await self.crawler.wait_for_selector(
            "#filter-container.loaded", config=self.filter_config
        )

        # Apply filters with custom configuration
        for step in self.config.strategy_config.filtering_config.steps:
            try:
                if step.action == "click":
                    # Ensure element is visible and clickable
                    element = await self.crawler.wait_for_selector(
                        step.selector, config=self.filter_config
                    )
                    if element:
                        await element.click()
                        # Wait for results to update
                        await self.crawler.wait_for_selector(
                            ".results-container.updated", config=self.filter_config
                        )
                elif step.action == "input" and step.value:
                    await self.crawler.type(
                        step.selector, step.value, config=self.filter_config
                    )
                    # Trigger change event to update results
                    await self.crawler.eval_on_selector(
                        step.selector, "el => el.dispatchEvent(new Event('change'))"
                    )
            except Exception as e:
                print(f"Vesteda filter step '{step.step_name}' failed: {str(e)}")

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
