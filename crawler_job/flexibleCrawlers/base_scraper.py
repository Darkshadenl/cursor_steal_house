from typing import Dict, Any, AsyncGenerator, List, Optional
import os
from abc import ABC, abstractmethod

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawler_job.models.db_config_models import WebsiteConfig


class BaseWebsiteScraper(ABC):
    """Base class for website scrapers using the hybrid configuration system."""

    def __init__(self, crawler: AsyncWebCrawler, config: WebsiteConfig):
        """Initialize the scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
        """
        self.crawler = crawler
        self.config = config
        self.standard_run_config = self._build_standard_run_config()

    def _build_standard_run_config(self) -> CrawlerRunConfig:
        """Build the standard crawler run configuration.

        Returns:
            CrawlerRunConfig: The default configuration for crawl4ai.
        """
        return CrawlerRunConfig()

    async def login_async(self) -> bool:
        """Perform login if login configuration is provided.

        Returns:
            bool: True if login was successful or not required, False if login failed.
        """
        if not self.config.strategy_config.login_config:
            return True

        login_config = self.config.strategy_config.login_config
        try:
            # Navigate to login page
            await self.crawler.goto(
                login_config.login_page_url, config=self.standard_run_config
            )

            # Fill in credentials
            await self.crawler.type(
                login_config.username_selector,
                os.getenv("SCRAPER_USERNAME", ""),
                config=self.standard_run_config,
            )
            await self.crawler.type(
                login_config.password_selector,
                os.getenv("SCRAPER_PASSWORD", ""),
                config=self.standard_run_config,
            )

            # Submit form
            await self.crawler.click(
                login_config.submit_button_selector, config=self.standard_run_config
            )

            # Wait for success indicator
            success = await self.crawler.wait_for_selector(
                login_config.post_login_check_selector, config=self.standard_run_config
            )
            return success is not None

        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    async def navigate_to_gallery_async(self) -> None:
        """Navigate to the listings/gallery page."""
        await self.crawler.goto(
            self.config.strategy_config.navigation_config.listings_page_url,
            config=self.standard_run_config,
        )

    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.config.strategy_config.filtering_config:
            return

        for step in self.config.strategy_config.filtering_config.steps:
            try:
                if step.action == "click":
                    await self.crawler.click(
                        step.selector, config=self.standard_run_config
                    )
                elif step.action == "input" and step.value:
                    await self.crawler.type(
                        step.selector, step.value, config=self.standard_run_config
                    )
                elif step.action == "wait" and step.wait_condition:
                    if step.wait_condition["type"] == "selector":
                        await self.crawler.wait_for_selector(
                            step.wait_condition["selector"],
                            config=self.standard_run_config,
                        )
            except Exception as e:
                print(f"Filter step '{step.step_name}' failed: {str(e)}")

    async def extract_gallery_async(self) -> AsyncGenerator[Dict[str, Any], None]:
        """Extract data from the gallery/listings page.

        Yields:
            Dict[str, Any]: Extracted data for each listing item.
        """
        config = self.config.strategy_config.gallery_extraction_config
        page_count = 0

        while True:
            # Extract items from current page
            items = await self.crawler.query_selector_all(config.listing_item_selector)

            for item in items:
                result = {}
                for field in config.fields:
                    try:
                        element = await item.query_selector(field.selector)
                        if not element and field.is_required:
                            print(f"Required field '{field.target_field}' not found")
                            continue

                        if field.extraction_type == "text":
                            value = await element.text() if element else None
                        elif field.extraction_type == "html":
                            value = await element.inner_html() if element else None
                        elif (
                            field.extraction_type == "attribute"
                            and field.attribute_name
                        ):
                            value = (
                                await element.get_attribute(field.attribute_name)
                                if element
                                else None
                            )

                        if field.transformation_rule and value:
                            # Apply transformations (to be implemented based on rules)
                            pass

                        result[field.target_field] = value

                    except Exception as e:
                        print(
                            f"Error extracting field '{field.target_field}': {str(e)}"
                        )
                        if field.is_required:
                            break

                if result:
                    yield result

            # Check if we should proceed to next page
            page_count += 1
            if not config.next_page_selector or (
                config.max_pages and page_count >= config.max_pages
            ):
                break

            next_button = await self.crawler.query_selector(config.next_page_selector)
            if not next_button:
                break

            await next_button.click()
            await self.crawler.wait_for_navigation()

    async def extract_details_async(self, url: str) -> Dict[str, Any]:
        """Extract data from a detail page.

        Args:
            url: The URL of the detail page to scrape.

        Returns:
            Dict[str, Any]: The extracted data.
        """
        await self.crawler.goto(url, config=self.standard_run_config)
        result = {}

        for field in self.config.strategy_config.detail_page_extraction_config.fields:
            try:
                element = await self.crawler.query_selector(field.selector)
                if not element and field.is_required:
                    print(f"Required field '{field.target_field}' not found")
                    continue

                if field.extraction_type == "text":
                    value = await element.text() if element else None
                elif field.extraction_type == "html":
                    value = await element.inner_html() if element else None
                elif field.extraction_type == "attribute" and field.attribute_name:
                    value = (
                        await element.get_attribute(field.attribute_name)
                        if element
                        else None
                    )

                if field.transformation_rule and value:
                    # Apply transformations (to be implemented based on rules)
                    pass

                result[field.target_field] = value

            except Exception as e:
                print(f"Error extracting field '{field.target_field}': {str(e)}")
                if field.is_required:
                    break

        return result

    async def run_async(self) -> List[Dict[str, Any]]:
        """Run the complete scraping process.

        Returns:
            List[Dict[str, Any]]: The collected data from all listings.
        """
        results = []

        # Login if needed
        if not await self.login_async():
            print("Login failed, aborting scrape")
            return results

        # Navigate to gallery
        await self.navigate_to_gallery_async()

        # Apply filters
        await self.apply_filters_async()

        # Extract gallery items
        async for item in self.extract_gallery_async():
            if "url" in item:
                # Get details for each item
                details = await self.extract_details_async(item["url"])
                results.append({**item, **details})
            else:
                results.append(item)

        return results
