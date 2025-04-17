import os
import logging
import json
from typing import Dict, List, Optional, Any, Tuple
import asyncio
from urllib.parse import urljoin

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from playwright.async_api import ElementHandle

from crawler_job.models.house_models import House, FetchedPage
from crawler_job.models.config_models import WebsiteConfig, FieldMapping
from crawler_job.services.repositories.config_repository import WebsiteConfigRepository
from crawler_job.services.house_service import HouseService
from crawler_job.services.llm_service import LLMService, LLMProvider
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.crawlers.base_scraper import AbstractWebsiteScraper


logger = logging.getLogger(__name__)


class ConfigurableWebsiteScraper(AbstractWebsiteScraper):
    """
    Configurable website scraper implementation that uses configuration from the database.
    """

    def __init__(
        self,
        crawler: AsyncWebCrawler,
        config_repository: WebsiteConfigRepository,
        house_service: HouseService,
        llm_service: LLMService,
        notification_service: Optional[NotificationService] = None,
    ):
        """
        Initialize the configurable website scraper.

        Args:
            crawler: AsyncWebCrawler instance for browser automation
            config_repository: Repository for loading website configurations
            house_service: Service for house data storage and retrieval
            llm_service: Service for LLM-based data extraction
            notification_service: Optional service for sending notifications
        """
        self.crawler = crawler
        self.config_repo = config_repository
        self.house_service = house_service
        self.llm_service = llm_service
        self.notification_service = notification_service
        self.config = None
        self.session_id = None
        self.logger = logging.getLogger(__name__)

    async def load_config_async(self, website_id: int) -> None:
        """
        Load the website configuration from the database.

        Args:
            website_id: ID of the website to load configuration for
        """
        self.config = await self.config_repo.get_config_async(website_id)
        self.session_id = f"{self.config.website_info.name.lower()}_session"

        # Log loaded configuration
        self.logger.info(
            f"Loaded configuration for website: {self.config.website_info.name}"
        )

        # Validate configuration
        if not self.config.navigation_config:
            raise ValueError(
                f"Navigation configuration is missing for website ID {website_id}"
            )

        if not self.config.gallery_extraction_config:
            raise ValueError(
                f"Gallery extraction configuration is missing for website ID {website_id}"
            )

    async def login_async(self) -> bool:
        """
        Log in to the website if required.

        Returns:
            bool: True if login was successful or not needed, False otherwise
        """
        if not self.config or not self.config.login_config:
            self.logger.info("No login configuration found, skipping login")
            return True

        if not self.config.login_config.needs_login:
            self.logger.info("Login not required for this website")
            return True

        # Get credentials from environment variables
        credential_source = self.config.login_config.credential_source
        if credential_source.startswith("env:"):
            env_var = credential_source.split(":", 1)[1]
            username = os.getenv(f"{env_var}")
            password = os.getenv(f"{env_var}_PASSWORD")

            if not username or not password:
                raise ValueError(
                    f"Missing credentials in environment variables: {env_var} and/or {env_var}_PASSWORD"
                )
        else:
            raise ValueError(f"Unsupported credential source: {credential_source}")

        # Build the login URL
        base_url = self.config.website_info.base_url
        login_path = self.config.login_config.login_url_path or "/login"
        login_url = urljoin(base_url, login_path)

        self.logger.info(f"Logging in to {login_url}")

        # Set up run config for login
        run_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            magic=True,
            js_code=[
                f"document.querySelector('{self.config.login_config.username_selector}').value = '{username}';",
                f"document.querySelector('{self.config.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.config.login_config.submit_selector}').click();",
            ],
        )

        # Execute login
        login_result = await self.crawler.arun(url=login_url, config=run_config)

        if not login_result.success:
            self.logger.error(f"Login failed: {login_result.error_message}")
            return False

        # Verify login success if a success indicator is provided
        if self.config.login_config.success_indicator_selector:
            # Wait a moment for the redirect to complete
            await asyncio.sleep(2)

            check_config = CrawlerRunConfig(
                session_id=self.session_id,
                cache_mode=CacheMode.BYPASS,
                js_only=True,
            )

            check_result = await self.crawler.arun(url=base_url, config=check_config)

            if not check_result.success:
                self.logger.error(
                    f"Login verification failed: {check_result.error_message}"
                )
                return False

            # Check for success indicator
            success_indicator_js = f"""
                !!document.querySelector('{self.config.login_config.success_indicator_selector}')
            """

            success_result = await self.crawler.aeval(success_indicator_js)

            if not success_result:
                self.logger.error(
                    "Login verification failed: Success indicator not found"
                )
                return False

        self.logger.info("Login successful")
        return True

    async def navigate_to_gallery_async(self) -> str:
        """
        Navigate to the gallery/search page with all property listings.

        Returns:
            str: URL of the gallery page
        """
        if not self.config or not self.config.navigation_config:
            raise ValueError("Navigation configuration is missing")

        # Build the gallery URL
        base_url = self.config.website_info.base_url
        gallery_path = self.config.navigation_config.gallery_url_path
        gallery_url = urljoin(base_url, gallery_path)

        self.logger.info(f"Navigating to gallery page: {gallery_url}")

        # Set up run config for navigation
        run_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            js_only=True,
        )

        # Navigate to gallery page
        gallery_result = await self.crawler.arun(url=gallery_url, config=run_config)

        if not gallery_result.success:
            raise Exception(
                f"Navigation to gallery failed: {gallery_result.error_message}"
            )

        # Execute additional navigation steps if configured
        if self.config.navigation_config.steps:
            self.logger.info("Executing additional navigation steps")

            for step in self.config.navigation_config.steps:
                action_type = step.get("action")
                selector = step.get("selector")

                if not action_type or not selector:
                    self.logger.warning(f"Skipping invalid step: {step}")
                    continue

                if action_type == "click":
                    click_js = f"""
                        document.querySelector('{selector}').click();
                        true
                    """

                    click_result = await self.crawler.aeval(click_js)

                    if not click_result:
                        self.logger.warning(
                            f"Click step failed for selector: {selector}"
                        )

                    # Wait a moment for the click to take effect
                    await asyncio.sleep(1)

                elif action_type == "wait":
                    # Wait for the selector to appear
                    wait_time = step.get("wait_time", 5)
                    await asyncio.sleep(wait_time)

                else:
                    self.logger.warning(f"Unknown action type: {action_type}")

        # Return the final URL
        return gallery_result.url

    async def extract_gallery_async(self) -> List[House]:
        """
        Extract property listings from the gallery/search results page.

        Returns:
            List[House]: List of extracted house objects with basic information
        """
        if not self.config or not self.config.gallery_extraction_config:
            raise ValueError("Gallery extraction configuration is missing")

        gallery_config = self.config.gallery_extraction_config
        extraction_method = gallery_config.extraction_method

        self.logger.info(f"Extracting gallery using method: {extraction_method}")

        houses = []

        if extraction_method in ["css", "xpath"]:
            # Use CSS/XPath selectors for extraction
            if not gallery_config.base_selector:
                raise ValueError("Base selector is missing for CSS/XPath extraction")

            if not gallery_config.field_mappings:
                raise ValueError("Field mappings are missing for CSS/XPath extraction")

            # Get the elements matching the base selector
            selector_type = "css" if extraction_method == "css" else "xpath"
            elements = await self._get_elements(
                gallery_config.base_selector, selector_type
            )

            self.logger.info(f"Found {len(elements)} property listings on the page")

            for element in elements:
                # Extract fields according to mappings
                data = await self._apply_field_mappings(
                    element, gallery_config.field_mappings
                )

                # Create House object if required fields are present
                if "address" in data and "city" in data and "status" in data:
                    house = House.from_dict(data)
                    houses.append(house)
                else:
                    self.logger.warning(f"Skipping incomplete listing: {data}")

            # Handle pagination if configured
            if (
                gallery_config.next_page_selector
                and self.config.navigation_config.next_page_selector
            ):
                # TODO: Implement pagination
                pass

        elif extraction_method == "llm":
            # Use LLM for extraction
            if not gallery_config.llm_provider or not gallery_config.llm_instruction:
                raise ValueError(
                    "LLM provider and instruction are required for LLM extraction"
                )

            # Get page HTML
            html_result = await self.crawler.aeval("document.documentElement.outerHTML")

            if not html_result:
                raise Exception("Failed to get page HTML for LLM extraction")

            # Convert provider string to enum
            provider = LLMProvider(gallery_config.llm_provider)

            # Get schema
            schema = House.model_json_schema()

            # Extract with LLM
            extracted_data = await self.llm_service.extract(
                html_result, schema, provider
            )

            if extracted_data:
                try:
                    json_data = json.loads(extracted_data)
                    # Create House directly from the dict
                    house = House.from_dict(json_data)
                    houses.append(house)
                except Exception as e:
                    self.logger.error(f"Error parsing LLM extraction result: {str(e)}")

        else:
            raise ValueError(f"Unsupported extraction method: {extraction_method}")

        self.logger.info(f"Extracted {len(houses)} houses from gallery")
        return houses

    async def extract_details_async(self, gallery_item: House) -> Optional[House]:
        """
        Extract detailed information for a specific property.

        Args:
            gallery_item: House object with basic information from the gallery

        Returns:
            Optional[House]: Complete House object with all available details, or None if extraction failed
        """
        if not gallery_item.detail_url:
            self.logger.warning(f"No detail URL for house: {gallery_item.address}")
            return None

        if not self.config or not self.config.detail_extraction_config:
            self.logger.warning("Detail extraction configuration is missing")
            return gallery_item

        detail_config = self.config.detail_extraction_config
        extraction_method = detail_config.extraction_method

        self.logger.info(
            f"Extracting details for {gallery_item.address} using method: {extraction_method}"
        )

        # Navigate to detail page
        detail_url = gallery_item.detail_url
        if not detail_url.startswith("http"):
            detail_url = urljoin(self.config.website_info.base_url, detail_url)

        run_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            js_only=True,
        )

        detail_result = await self.crawler.arun(url=detail_url, config=run_config)

        if not detail_result.success:
            self.logger.error(
                f"Failed to navigate to detail page: {detail_result.error_message}"
            )
            return None

        detailed_house = None

        if extraction_method in ["css", "xpath"]:
            # Use CSS/XPath selectors for extraction
            if not detail_config.field_mappings:
                self.logger.warning(
                    "Field mappings are missing for CSS/XPath extraction"
                )
                return gallery_item

            # Extract fields according to mappings
            page_element = await self._get_document_element()
            data = await self._apply_field_mappings(
                page_element, detail_config.field_mappings
            )

            # Ensure required fields are preserved from gallery item
            data["address"] = gallery_item.address
            data["city"] = gallery_item.city
            data["status"] = gallery_item.status
            data["detail_url"] = gallery_item.detail_url

            # Create detailed House object
            detailed_house = House.from_dict(data)

        elif extraction_method == "llm":
            # Use LLM for extraction
            if not detail_config.llm_provider:
                self.logger.warning("LLM provider is missing for LLM extraction")
                return gallery_item

            # Get page HTML or markdown
            html_result = await self.crawler.aeval("document.documentElement.outerHTML")

            if not html_result:
                self.logger.error("Failed to get page HTML for LLM extraction")
                return gallery_item

            # Create FetchedPage object
            fetched_page = FetchedPage(
                url=detail_url, markdown=html_result, success=True
            )

            # Convert provider string to enum
            provider = LLMProvider(detail_config.llm_provider)

            # Get schema
            schema = House.model_json_schema()

            # Extract with LLM
            extracted_data = await self.llm_service.extract(
                fetched_page.markdown, schema, provider
            )

            if extracted_data:
                try:
                    json_data = json.loads(extracted_data)
                    # Create House from the dict
                    detailed_house = House.from_dict(json_data)

                    # Ensure required fields are preserved from gallery item
                    if not detailed_house.address:
                        detailed_house.address = gallery_item.address
                    if not detailed_house.city:
                        detailed_house.city = gallery_item.city
                    if not detailed_house.status:
                        detailed_house.status = gallery_item.status
                    if not detailed_house.detail_url:
                        detailed_house.detail_url = gallery_item.detail_url

                except Exception as e:
                    self.logger.error(f"Error parsing LLM extraction result: {str(e)}")
                    return gallery_item
            else:
                self.logger.warning("LLM extraction returned no data")
                return gallery_item

        else:
            self.logger.warning(f"Unsupported extraction method: {extraction_method}")
            return gallery_item

        # Merge with gallery item
        if detailed_house:
            # For any fields that are None in detailed_house, use values from gallery_item
            for field, value in gallery_item.model_dump().items():
                if getattr(detailed_house, field) is None and value is not None:
                    setattr(detailed_house, field, value)

            self.logger.info(
                f"Successfully extracted details for {gallery_item.address}"
            )
            return detailed_house

        return gallery_item

    async def run_async(self, website_id: int) -> Dict[str, Any]:
        """
        Run the complete scraping process.

        Args:
            website_id: ID of the website to scrape

        Returns:
            Dict[str, Any]: Results of the scraping process
        """
        try:
            # Load configuration
            await self.load_config_async(website_id)

            # Log in if required
            login_success = await self.login_async()
            if not login_success:
                raise Exception("Login failed")

            # Navigate to gallery page
            gallery_url = await self.navigate_to_gallery_async()
            self.logger.info(f"Successfully navigated to gallery: {gallery_url}")

            # Extract gallery listings
            houses = await self.extract_gallery_async()
            self.logger.info(f"Extracted {len(houses)} houses from gallery")

            if not houses:
                self.logger.warning("No houses found in gallery")
                return {
                    "website_id": website_id,
                    "website_name": self.config.website_info.name,
                    "total_houses_count": 0,
                    "new_houses_count": 0,
                    "existing_houses_count": 0,
                    "updated_houses_count": 0,
                    "success": True,
                }

            # Identify new houses
            new_houses = await self.house_service.identify_new_houses_async(houses)
            self.logger.info(f"Found {len(new_houses)} new houses")

            # Extract details for new houses
            if new_houses:
                self.logger.info(f"Extracting details for {len(new_houses)} new houses")

                for i, house in enumerate(new_houses):
                    self.logger.info(
                        f"Extracting details for house {i+1}/{len(new_houses)}: {house.address}"
                    )
                    detailed_house = await self.extract_details_async(house)

                    if detailed_house:
                        # Update the house in the main list
                        for j, main_house in enumerate(houses):
                            if (
                                main_house.address == house.address
                                and main_house.city == house.city
                            ):
                                houses[j] = detailed_house
                                break

            # Store houses in database
            result = await self.house_service.store_houses_atomic_async(
                houses=houses,
                all_houses=houses,
            )

            return {
                "website_id": website_id,
                "website_name": self.config.website_info.name,
                "total_houses_count": len(houses),
                "new_houses_count": result["new_count"],
                "existing_houses_count": result["existing_count"],
                "updated_houses_count": result.get("updated_count", 0),
                "success": True,
            }

        except Exception as e:
            self.logger.error(f"Error during scraping: {str(e)}")
            return {
                "website_id": website_id,
                "website_name": (
                    self.config.website_info.name if self.config else "Unknown"
                ),
                "error": str(e),
                "success": False,
            }

    # Helper methods

    async def _get_elements(
        self, selector: str, selector_type: str = "css"
    ) -> List[ElementHandle]:
        """
        Get elements from the page using the specified selector.

        Args:
            selector: CSS or XPath selector
            selector_type: Type of selector ('css' or 'xpath')

        Returns:
            List[ElementHandle]: List of matching elements
        """
        if selector_type == "css":
            js_code = f"""
                Array.from(document.querySelectorAll('{selector}'))
            """
        elif selector_type == "xpath":
            js_code = f"""
                Array.from(document.evaluate('{selector}', document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null))
            """
        else:
            raise ValueError(f"Unsupported selector type: {selector_type}")

        elements = await self.crawler.aeval(js_code)
        return elements or []

    async def _get_document_element(self) -> ElementHandle:
        """
        Get the document element.

        Returns:
            ElementHandle: Document element
        """
        return await self.crawler.aeval("document.documentElement")

    async def _apply_field_mappings(
        self, element: ElementHandle, mappings: List[FieldMapping]
    ) -> Dict[str, Any]:
        """
        Apply field mappings to extract data from an element.

        Args:
            element: Element to extract data from
            mappings: List of field mappings

        Returns:
            Dict[str, Any]: Extracted data
        """
        data = {}

        for mapping in mappings:
            value = None

            try:
                selector = mapping.selector
                selector_type = mapping.selector_type
                extraction_type = mapping.extraction_type

                if selector_type == "css":
                    js_prefix = f"document.querySelector('{selector}')"
                elif selector_type == "xpath":
                    js_prefix = f"document.evaluate('{selector}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue"
                else:
                    self.logger.warning(f"Unsupported selector type: {selector_type}")
                    continue

                if extraction_type == "text":
                    js_code = f"{js_prefix}?.textContent?.trim()"
                elif extraction_type == "html":
                    js_code = f"{js_prefix}?.innerHTML?.trim()"
                elif extraction_type == "attribute":
                    if not mapping.attribute_name:
                        self.logger.warning(
                            "Attribute name is missing for attribute extraction"
                        )
                        continue
                    js_code = f"{js_prefix}?.getAttribute('{mapping.attribute_name}')"
                else:
                    self.logger.warning(
                        f"Unsupported extraction type: {extraction_type}"
                    )
                    continue

                # Execute JavaScript to extract the value
                value = await self.crawler.aeval(js_code)

                # Handle empty values
                if value is None or value == "":
                    if mapping.is_required and mapping.default_value is not None:
                        value = mapping.default_value
                    elif mapping.is_required:
                        self.logger.warning(
                            f"Required field {mapping.pydantic_field_name} is missing"
                        )
                        continue

                # Store extracted value
                data[mapping.pydantic_field_name] = value

            except Exception as e:
                self.logger.error(
                    f"Error extracting field {mapping.pydantic_field_name}: {str(e)}"
                )
                if mapping.is_required and mapping.default_value is not None:
                    data[mapping.pydantic_field_name] = mapping.default_value

        return data


__all__ = ["ConfigurableWebsiteScraper"]
