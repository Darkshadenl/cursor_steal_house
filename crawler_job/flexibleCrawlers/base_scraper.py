from enum import Enum
import json
from typing import Dict, Any, List, Optional
import os
from abc import ABC
import asyncio
import re

from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlResult,
    CrawlerMonitor,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy,
    PruningContentFilter,
    RateLimiter,
    SemaphoreDispatcher,
)
from crawler_job.models.db_config_models import (
    CookiesConfig,
    DetailPageExtractionConfig,
    FilteringConfig,
    GalleryExtractionConfig,
    LoginConfig,
    SitemapExtractionConfig,
    WebsiteConfig,
)
from crawler_job.models.house_models import House, FetchedPage
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services import llm_service
from crawler_job.services.house_service import HouseService
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class BaseWebsiteScraper(ABC):
    """Base class for website scrapers using the hybrid configuration system."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
        debug_mode: bool = False,
    ):
        """Initialize the scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
            notification_service: The notification service to use.
        """
        self.website_config: WebsiteConfig = config
        self.notification_service = notification_service
        self.debug_mode = debug_mode

        self.login_config: LoginConfig = self.website_config.strategy_config.login_config  # type: ignore

        self.detail_page_extraction_config: DetailPageExtractionConfig = (
            self.website_config.strategy_config.detail_page_extraction_config
        )  # type: ignore

        self.gallery_extraction_config: GalleryExtractionConfig = (
            self.website_config.strategy_config.gallery_extraction_config
        )  # type: ignore

        self.sitemap_extraction_config: SitemapExtractionConfig = (
            self.website_config.strategy_config.sitemap_extraction_config
        )  # type: ignore

        self.filtering_config: FilteringConfig = (
            self.website_config.strategy_config.filtering_config
        )  # type: ignore

        self.cookies_config: CookiesConfig = (
            self.website_config.strategy_config.cookies_config
        )  # type: ignore

        self.session_id = session_id

        self.standard_run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            log_console=self.debug_mode,
            js_only=False,
            magic=False,
            exclude_all_images=True,
            exclude_social_media_links=True,
            user_agent_mode="random",
        )

        self.standard_dispatcher = SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=True),
            rate_limiter=RateLimiter(
                base_delay=(3.0, 5.0),
                max_delay=30.0,
                max_retries=3,
                rate_limit_codes=[429, 503],
            ),
        )

        self.crawler: AsyncWebCrawler = crawler
        self.accepted_cookies = False
        self.navigated_to_gallery = False
        self.navigated_to_sitemap = False
        self.current_url = ""
        self.default_results = {
            "success": False,
            "total_houses_count": 0,
            "new_houses_count": 0,
            "updated_houses_count": 0,
        }

    async def validate_current_page(self, expected_url: str, check_url: str) -> bool:
        """Validate if the current page is the expected page.

        Args:
            expected_url: The expected URL to validate against.

        Returns:
            bool: True if the current page is the expected page, False otherwise.
        """
        if not self.crawler:
            raise Exception("Crawler not initialized")

        check_config = CrawlerRunConfig(
            session_id=self.session_id,
            cache_mode=CacheMode.BYPASS,
            log_console=self.debug_mode,
            js_only=False,
            magic=False,
            user_agent_mode="random",
        )

        logger.info(f"Verifying... Expected URL: {expected_url}")

        check_result: CrawlResult = await self.crawler.arun(
            url=check_url, config=check_config
        )  # type: ignore

        if not check_result.success:
            raise Exception(f"Check verification failed: {check_result.error_message}")

        # logger.debug(f"Check result: {check_result}")

        if (
            check_result.url != expected_url
            and check_result.redirected_url != expected_url
        ):
            raise Exception(f"Verification failed: We're not on the expected page")

        return True

    async def login_async(self) -> bool:
        """Perform login if login configuration is provided.

        Returns:
            bool: True if login was successful or not required, False if login failed.
        """
        if not self.login_config or (
            self.navigated_to_gallery and not self.login_config.login_required
        ):
            logger.warn(f"Skipping login for {self.website_config.website_name}")
            return True

        if not self.crawler:
            raise Exception("Crawler not initialized")

        if not self.accepted_cookies:
            await self._accept_cookies(self.current_url or self.website_config.base_url)  # type: ignore

        try:
            base_url = self.website_config.base_url
            full_login_url = ""

            if self.login_config.login_url:
                full_login_url = self.login_config.login_url
            else:
                login_url_path = self.login_config.login_url_path
                full_login_url = f"{base_url}{login_url_path}"

            logger.info(
                f"Navigating to login page of {self.website_config.website_name} and logging in."
            )
            email = os.getenv(self.website_config.website_identifier.upper() + "_EMAIL")
            password = os.getenv(
                self.website_config.website_identifier.upper() + "_PASSWORD"
            )

            js_code = [
                f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.login_config.submit_selector}').click();",
            ]

            # Configure wait condition based on login config
            wait_for_condition = None
            if self.login_config.success_indicator_selector:
                wait_for_condition = (
                    f"css:{self.login_config.success_indicator_selector}"
                )
            elif self.login_config.expected_url:
                # Wait for URL change or a reasonable delay
                wait_for_condition = (
                    "js:() => window.location.pathname !== '"
                    + (self.login_config.login_url_path or "")
                    + "'"
                )
            else:
                wait_for_condition = ""

            run_config = CrawlerRunConfig(
                session_id=self.session_id,
                exclude_all_images=True,
                exclude_social_media_links=True,
                cache_mode=CacheMode.BYPASS,
                js_only=False,
                magic=False,
                js_code=js_code,
                wait_for=wait_for_condition,
                page_timeout=10000,  # 10 seconds timeout
                log_console=self.debug_mode,
            )

            login_result: CrawlResult = await self.crawler.arun(
                full_login_url, config=run_config
            )  # type: ignore

            if not login_result.success:
                if (
                    login_result.error_message
                    and "Page.content: Unable to retrieve content because the page is navigating and changing the content"
                    in login_result.error_message
                ):
                    logger.info(
                        f"Navigation in progress detected. Waiting for page to stabilize for {self.website_config.website_name}."
                    )

                    # Try again with a different wait strategy
                    stabilize_config = CrawlerRunConfig(
                        session_id=self.session_id,
                        cache_mode=CacheMode.BYPASS,
                        js_only=True,
                        wait_for="domcontentloaded",
                        page_timeout=15000,
                        log_console=self.debug_mode,
                    )

                    stabilize_result: CrawlResult = await self.crawler.arun(
                        self.current_url or full_login_url, config=stabilize_config
                    )  # type: ignore

                    if stabilize_result.success:
                        logger.info(
                            f"Page stabilized successfully for {self.website_config.website_name}"
                        )
                        self.current_url = stabilize_result.url
                        return True
                    else:
                        logger.warning(
                            f"Page stabilization attempt failed: {stabilize_result.error_message}"
                        )
                        return (
                            True  # Assume login succeeded despite stabilization issues
                        )
                else:
                    raise Exception(
                        f"Login form submission failed: {login_result.error_message}"
                    )

            self.current_url = login_result.url
            return True

        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False

    async def navigate_to_sitemap_async(self) -> str:
        if self.navigated_to_sitemap:
            raise Exception(
                "Already navigated to sitemap. How? Something must be wrong."
            )

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info(f"Navigating to and extracting sitemap...")
        url = f"{self.website_config.base_url}{self.website_config.strategy_config.navigation_config.sitemap}"

        result: CrawlResult = await self.crawler.arun(
            url,
            config=self.standard_run_config,
        )  # type: ignore

        if not result.success:
            raise Exception(f"Failed to navigate to sitemap: {result.error_message}")

        full_sitemap_url = f"{self.website_config.base_url}{self.website_config.strategy_config.navigation_config.sitemap}"

        if result.redirected_url == full_sitemap_url or result.url == full_sitemap_url:
            self.navigated_to_sitemap = True
            self.current_url = result.url
            logger.info(f"Navigated to sitemap: {result.url}")
            return result.html
        else:
            self.navigated_to_sitemap = False
            raise Exception(f"Failed to navigate to sitemap: {result.error_message}")

    async def navigate_to_gallery_async(self, force_navigation: bool = False) -> None:
        """Navigate to the listings/gallery page."""
        if self.navigated_to_gallery and not force_navigation:
            return

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info(f"Navigating to gallery...")
        url = f"{self.website_config.base_url}{self.website_config.strategy_config.navigation_config.gallery}"

        result: CrawlResult = await self.crawler.arun(
            url,
            config=self.standard_run_config,
        )  # type: ignore

        full_login_url = (
            f"{self.website_config.base_url}{self.login_config.login_url_path or ''}"
        )

        if result and result.success and result.redirected_url != full_login_url:
            logger.info(f"Navigating to gallery successful: {result.url}")
            self.navigated_to_gallery = True
            self.current_url = result.url
        else:
            self.current_url = result.redirected_url
            logger.error(f"Navigating to gallery failed: {result.error_message}")
            logger.error(f"Redirected URL: {result.redirected_url}")

    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.filtering_config:
            logger.info("No filtering configuration provided.")
            return

        js = """
(async () => {
    try {
        const searchContainer = await new Promise((resolve, reject) => {
            const timeout = 5000;
            const interval = 100;
            const startTime = Date.now();
            
            const check = () => {
                const element = document.querySelector('.search-default');
                if (element) {
                    resolve(element);
                    return;
                }
                
                if (Date.now() - startTime >= timeout) {
                    reject(new Error('Search container not found within 5s'));
                    return;
                }
                
                setTimeout(check, interval);
            };
            
            check();
        });

        const addressInput = searchContainer.querySelector('.search-field--adres input');
        addressInput.value = 'Tilburg';
        
        const searchButton = searchContainer.querySelector('.search-field--button button');
        searchButton.click();
        
    } catch (error) {
        console.error('Fout bij zoeken:', error);
    }
})();

        """

        cookie_config = self.standard_run_config.clone()
        cookie_config.js_code = js
        cookie_config.log_console = True
        cookie_config.js_only = True
        if self.filtering_config.filters_container_selector:
            cookie_config.css_selector = (
                self.filtering_config.filters_container_selector
            )

        result = await self.crawler.arun(
            url=self.current_url,  # type: ignore
            config=cookie_config,
        )

        logger.info("Applied filters")

    async def extract_sitemap_async(self, sitemap_html: str) -> List[House]:
        """
        Fetch the sitemap page using an HTTP request, apply the configured regex, and return a list of House objects.

        Returns:
            List[House]: List of extracted House objects from the sitemap.
        """
        regex = self.sitemap_extraction_config.regex
        schema = self.sitemap_extraction_config.schema
        llm_instructions = self.sitemap_extraction_config.extra_llm_instructions

        if not regex or not schema:
            raise Exception("No regex or schema provided for sitemap extraction")

        logger.info(f"Extracting sitemap with regex: {regex}")

        urls = re.findall(regex, sitemap_html)
        logger.info(
            "Done with regex. Let's check if it already exists in the database!"
        )

        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            existing_houses = await house_service.get_houses_by_detail_url_async(urls)
            logger.info(f"Found {len(existing_houses)} existing houses")
            if existing_houses:
                existing_urls = {house.detail_url for house in existing_houses}
                urls = [url for url in urls if url not in existing_urls]

        dispatcher = SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=False),
            rate_limiter=RateLimiter(
                base_delay=(3.0, 5.0),
                max_delay=30.0,
                max_retries=3,
                rate_limit_codes=[429, 503],
            ),
        )
        config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(schema),
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            magic=False,
            user_agent_mode="random",
            log_console=self.debug_mode,
            exclude_all_images=True,
            exclude_social_media_links=True,
        )

        houses: List[House] = []
        schema = House.model_json_schema()
        llm_service = LLMService()

        try:
            logger.info(f"Running the crawler for {len(urls)} URLs...")
            results: List[CrawlResult] = await self.crawler.arun_many(
                urls=urls, config=config, dispatcher=dispatcher
            )  # type: ignore

            for result in results:
                if not result.success:
                    raise Exception(
                        f"Failed to extract property listings: {result.error_message}"
                    )
                if not result.extracted_content:
                    raise Exception("No extracted content")

                data = json.loads(result.extracted_content)
                data_str = json.dumps(data, indent=2, ensure_ascii=False)
                logger.info(
                    f"Extracting data from the crawler using LLM for {result.url}..."
                )
                extra_instructions = f"Determine for yourself if the property is a parking spot and fill in is_parkingspot based on that. \n The detail url is: {result.url}\n {llm_instructions}"
                extracted_data: Optional[Dict[str, Any]] = await llm_service.extract(
                    data_str,
                    schema,
                    LLMProvider.GEMINI,
                    extra_instructions=extra_instructions,
                )
                logger.info(
                    f"Done extracting data from the crawler using LLM for {result.url}."
                )
                if extracted_data is None:
                    logger.warning(f"No data extracted for {result.url}")
                    continue
                json_data = json.loads(extracted_data)  # type: ignore
                house = House.from_dict(json_data)
                houses.append(house)

        except Exception as e:
            raise e

        logger.info(f"Extracted {len(houses)} houses from sitemap using regex.")

        return houses

    async def extract_gallery_async(self) -> List[House]:
        if not self.navigated_to_gallery:
            raise Exception("Not navigated to gallery")

        if not self.website_config.strategy_config.gallery_extraction_config:
            raise Exception("No gallery extraction configuration provided.")

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info(
            f"Extracting property listings of {self.website_config.website_name} step..."
        )
        gallery_extraction_config = (
            self.website_config.strategy_config.gallery_extraction_config
        )

        if not gallery_extraction_config.correct_urls_paths:
            raise Exception("No correct URLs provided")

        correct_urls = [
            f"{self.website_config.base_url}{path}"
            for path in gallery_extraction_config.correct_urls_paths
        ]

        if not any(correct_url in self.current_url for correct_url in correct_urls):  # type: ignore
            raise Exception(f"Invalid URL: {self.current_url}")

        schema = gallery_extraction_config.schema

        if not schema:
            raise Exception("No schema provided")

        extraction_strategy = None
        if self.gallery_extraction_config.schema_type == SchemaType.XPATH.value:
            extraction_strategy = JsonXPathExtractionStrategy(schema)
        else:
            extraction_strategy = JsonCssExtractionStrategy(schema)

        config = self.standard_run_config.clone()
        config.extraction_strategy = extraction_strategy
        config.wait_for = "domcontentloaded"

        if self.gallery_extraction_config.gallery_container_selector:
            config.css_selector = (
                self.gallery_extraction_config.gallery_container_selector
            )

        logger.debug(f"Extracting gallery from url: {self.current_url}")
        result: CrawlResult = await self.crawler.arun(url=self.current_url, config=gallery_config)  # type: ignore

        if not result.success:
            raise Exception(
                f"Failed to extract property listings: {result.error_message}"
            )

        if not result.extracted_content:
            raise Exception("No extracted content")

        raw_data = json.loads(result.extracted_content)
        houses = []

        for house_data in raw_data:
            house = House.from_dict(house_data)
            houses.append(house)

        logger.info(f"Successfully extracted {len(houses)} properties")
        return houses

    async def extract_fetched_pages_async(
        self, houses: List[House]
    ) -> List[FetchedPage]:
        """
        Extract detailed property information for the given houses

        Args:
            houses: List of House objects with basic info

        Returns:
            List[FetchedPage]: List of fetched detail pages
        """
        extraction_type = self.detail_page_extraction_config.schema_type
        if not self.crawler:
            raise Exception("Crawler not initialized")
        if extraction_type not in ["llm"]:
            raise Exception("Invalid extraction type")

        logger.info("Starting detailed property extraction...")

        prune_filter = PruningContentFilter(
            # Lower → more content retained, higher → more content pruned
            threshold=0.45,
            threshold_type="dynamic",
            min_word_threshold=3,
        )
        config = CrawlerRunConfig(
            log_console=self.debug_mode,
            exclude_domains=self.detail_page_extraction_config.ignore_domains or [],
            mean_delay=1,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=prune_filter,
            ),
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            js_only=False,
            magic=True,
            user_agent_mode="random",
            exclude_all_images=True,
            exclude_social_media_links=True,
        )

        dispatcher = SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=True),
            rate_limiter=RateLimiter(
                base_delay=(3.0, 5.0),
                max_delay=30.0,
                max_retries=3,
                rate_limit_codes=[429, 503],
            ),
        )

        urls = []
        for house in houses:
            if house.detail_url:
                url = f"{self.website_config.base_url}{house.detail_url}"
                urls.append(url)

        logger.info(f"Starting fetch for {len(urls)} properties...")

        try:
            results: List[CrawlResult] = await self.crawler.arun_many(
                urls=urls, config=config, dispatcher=dispatcher
            )  # type: ignore

            fetched_pages = []
            for result in results:
                if result.success:
                    fetched_pages.append(
                        FetchedPage(
                            url=result.url,
                            markdown=result.markdown.raw_markdown,  # type: ignore
                            success=True,
                        )
                    )
                else:
                    error_msg = (
                        result.error_message
                        if hasattr(result, "error_message")
                        else "Unknown error"
                    )
                    logger.error(f"Error fetching property: {error_msg}")
                    fetched_pages.append(
                        FetchedPage(url=result.url, markdown="", success=False)
                    )

            logger.info(
                f"Completed fetching property pages. Successfully fetched {sum(1 for page in fetched_pages if page.success)} out of {len(urls)} properties."
            )
            return fetched_pages
        except Exception as e:
            logger.error(
                f"Critical error during detailed property extraction: {str(e)}"
            )
            return [FetchedPage(url=url, markdown="", success=False) for url in urls]

    async def process_details_xpath_css(self, houses: List[House]) -> List[House]:
        logger.info(f"Processing details with xpath/css for {len(houses)} houses...")

        config = self.standard_run_config
        schema = self.detail_page_extraction_config.schema
        dispatcher = self.standard_dispatcher
        dispatcher.semaphore_count = 1

        extraction_strategy = None
        if self.gallery_extraction_config.schema_type == SchemaType.XPATH.value:
            extraction_strategy = JsonXPathExtractionStrategy(schema)  # type: ignore
        else:
            extraction_strategy = JsonCssExtractionStrategy(schema)  # type: ignore

        config.extraction_strategy = extraction_strategy
        config.css_selector = (
            self.detail_page_extraction_config.detail_container_selector or ""
        )

        all_detail_urls = [house.detail_url for house in houses]

        results: List[CrawlResult] = await self.crawler.arun_many(
            urls=all_detail_urls, config=config, dispatcher=self.standard_dispatcher  # type: ignore
        )
        done_houses: List[House] = []

        for result in results:
            if not result.success:
                logger.error(f"Error fetching property: {result.error_message}")
                continue
            if not result.extracted_content:
                logger.error(f"No extracted content for {result.url}")
                continue
            raw_data = json.loads(result.extracted_content)
            house = next((h for h in houses if h.detail_url == result.url), None)

            if house:
                detailed_house = house.from_dict(raw_data[0])

                for field, detailed_value in detailed_house.model_dump().items():
                    house_value = getattr(house, field, None)
                    if (
                        house_value is None or house_value == ""
                    ) and detailed_value not in (None, ""):
                        setattr(house, field, detailed_value)

                done_houses.append(house)

        return done_houses

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.cookies_config:
            logger.info("Accepting cookies not required.")
            return True
        if not self.crawler:
            raise Exception("Crawler not initialized")
        if self.accepted_cookies:
            logger.info("Cookies already accepted.")
            return self.accepted_cookies

        logger.info(f"Accepting cookies for {self.website_config.website_name}...")
        
        js = f"""
            (async () => {{
                const cookieButton = document.querySelector('{self.cookies_config.accept_cookies_selector}');
                
                if (cookieButton) {{
                    cookieButton.click();
                    console.log("Cookie button clicked");
                }} else {{
                    console.log("Cookie button not found");
                    return true;
                }}
                
                while (true) {{
                    await new Promise(resolve => setTimeout(resolve, 100)); // Wait 100ms
                    const cookieButton = document.querySelector('{self.cookies_config.accept_cookies_selector}');
                    if (cookieButton) {{
                        cookieButton.click();
                        console.log("Cookie button clicked");
                        return true;
                    }}
                }}
            }})();
            """

        cookie_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            magic=True,
            session_id=self.session_id,
            log_console=self.debug_mode,
            js_code=js,
        )

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

    async def _check_if_houses_exist(self, houses: List[House]) -> List[House]:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            new_houses = await house_service.identify_new_houses_async(houses)

            if not new_houses:
                return []

            logger.info(f"Fetching details for {len(new_houses)} new houses...")
            return new_houses

    def _merge_detailed_houses(
        self, houses: List[House], detailed_houses: List[House]
    ) -> None:
        for detailed_house in detailed_houses:
            for house in houses:
                if (
                    house.address == detailed_house.address
                    and house.city == detailed_house.city
                ):
                    for field, value in detailed_house.model_dump(
                        exclude_unset=True
                    ).items():
                        if value is not None and (
                            getattr(house, field) is None
                            or field not in ["address", "city", "status"]
                        ):
                            setattr(house, field, value)
                    break

    async def _store_houses(self, houses: List[House]) -> None:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            await house_service.store_houses_atomic_async(
                houses=houses,
            )

    async def execute_llm_extraction(
        self, fetched_pages: List[FetchedPage], provider: LLMProvider
    ) -> List[House]:
        """
        Extract structured data from markdown using LLM

        Args:
            fetched_pages: List of fetched detail pages
            provider: LLM provider to use

        Returns:
            List[House]: List of House objects with extracted data
        """
        llm_service = LLMService()
        schema = House.model_json_schema()
        houses: List[House] = []

        logger.info("Extracting structured data using LLM...")

        for page in fetched_pages:
            if not page.success:
                continue

            try:
                extracted_data: Optional[Dict[str, Any]] = await llm_service.extract(
                    page.markdown, schema, provider
                )

                if extracted_data is None:
                    logger.warning(f"No data extracted for {page.url}")
                    continue

                json_data = json.loads(extracted_data)  # type: ignore
                house = House.from_dict(json_data)
                houses.append(house)
                logger.info(f"Successfully extracted data for {page.url}")
            except Exception as e:
                logger.warning(f"Error extracting data for {page.url}: {str(e)}")
                continue

        return houses

    async def validate_login(self) -> bool:
        if not self.login_config.validate_login or self.navigated_to_gallery:
            logger.info(
                f"Skipping login validation for {self.website_config.website_name}"
            )
            return True

        await asyncio.sleep(2)
        logger.info(f"Validating login success of {self.website_config.website_name}")

        valid: bool = await self.validate_current_page(
            f"{self.website_config.base_url}{self.login_config.expected_url_path}",
            f"{self.website_config.base_url}{self.login_config.success_check_url_path}",
        )
        self.current_url = self.login_config.expected_url_path

        return valid

    async def run_gallery_scrape(self) -> Dict[str, Any]:
        await self.navigate_to_gallery_async()
        await self.login_async()

        if not await self.validate_login():
            logger.error("Login failed, aborting scrape")
            return self.default_results

        await self.navigate_to_gallery_async(force_navigation=True)
        await self.apply_filters_async()
        houses = await self.extract_gallery_async()
        new_houses: List[House] = await self._check_if_houses_exist(houses)

        if not new_houses or len(new_houses) == 0:
            logger.info("No new houses found, we're done here!")
            self.default_results["success"] = True
            return self.default_results

        detailed_houses = []
        if self.detail_page_extraction_config.schema_type in ["xpath", "css"]:
            detailed_houses = await self.process_details_xpath_css(new_houses)
        elif self.detail_page_extraction_config.schema_type == "llm":
            fetched_pages = await self.extract_fetched_pages_async(new_houses)
            detailed_houses = await self.execute_llm_extraction(
                fetched_pages, provider=LLMProvider.GEMINI
            )

        if not detailed_houses:
            logger.info("No detailed houses found. Exiting...")
            self.default_results["success"] = True
            return self.default_results

        self._merge_detailed_houses(houses, detailed_houses)

        await self._store_houses(houses)

        return {
            "success": True,
            "total_houses_count": len(houses),
            "new_houses_count": len(new_houses),
            "updated_houses_count": len(houses) - len(new_houses),
        }

    async def run_sitemap_scrape(self) -> Dict[str, Any]:
        await self.login_async()

        if not await self.validate_login():
            logger.error("Login failed, aborting scrape")
            return self.default_results

        sitemap_html = await self.navigate_to_sitemap_async()
        await self.apply_filters_async()
        houses = await self.extract_sitemap_async(sitemap_html)
        new_houses = await self._check_if_houses_exist(houses)
        await self._store_houses(new_houses)

        return {
            "success": True,
            "total_houses_count": len(houses),
            "new_houses_count": len(new_houses),
            "updated_houses_count": len(houses) - len(new_houses),
        }

    async def run_async(self) -> Dict[str, Any]:
        """Run the complete scraping process.

        Returns:
            List[Dict[str, Any]]: The collected data from all listings.
        """
        strategy = self.website_config.scrape_strategy

        logger.info(
            f"Choosing strategy {strategy} for {self.website_config.website_name}"
        )
        result = None

        if strategy == ScrapeStrategy.GALLERY.value:
            result = await self.run_gallery_scrape()
        elif strategy == ScrapeStrategy.SITEMAP.value:
            result = await self.run_sitemap_scrape()
        else:
            raise Exception(f"Invalid scrape strategy: {strategy}")

        return result


class ScrapeStrategy(Enum):
    GALLERY = "gallery"
    SITEMAP = "sitemap"


class SchemaType(Enum):
    XPATH = "xpath"
    CSS = "css"
    LLM = "llm"
