import json
from typing import Dict, Any, List, Optional
import os
from abc import ABC
import re

from crawler_job.enums import ScrapeStrategy, SchemaType
from crawler_job.helpers.decorators import (
    requires_crawler_initialized,
    requires_cookies_accepted,
    requires_login_config,
)
from crawler_job.helpers.config_validator import WebsiteConfigValidator
from crawler_job.helpers.crawler_config_factory import CrawlerConfigFactory


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
from crawler_job.models.pydantic_models import (
    CookiesConfig,
    DetailPageExtractionConfig,
    FilteringConfig,
    GalleryExtractionConfig,
    LoginConfig,
    SitemapExtractionConfig,
    StrategyConfig,
    WebsiteConfig,
    WebsiteScrapeConfigJson,
)
from crawler_job.models.house_models import House, FetchedPage
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.data_processing_service import DataProcessingService
from crawler_job.services.house_service import HouseService
from crawler_job.services.llm_extraction_service import LlmExtractionService
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger
from crawler_job.services import config as global_config

logger = setup_logger(__name__)


class BaseWebsiteScraper(ABC):
    """Base class for website scrapers using the hybrid configuration system."""

    def __init__(
        self,
        config: WebsiteScrapeConfigJson,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
    ):
        self.website_config: WebsiteScrapeConfigJson = config
        self.website_info: WebsiteConfig = self.website_config.website_info
        self.notification_service = notification_service
        self.logger = logger

        self.login_config: LoginConfig = self.website_config.strategy_config.login_config  # type: ignore
        self.strategy_config: StrategyConfig = self.website_config.strategy_config

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

        self._standard_run_config = CrawlerConfigFactory.create_standard_run_config(
            self.session_id, global_config.debug_mode
        )
        self.standard_dispatcher = CrawlerConfigFactory.create_standard_dispatcher()

        self.crawler: AsyncWebCrawler = crawler
        assert self.notification_service is not None
        self.data_processing_service = DataProcessingService(self.notification_service)
        self.llm_extraction_service = LlmExtractionService()
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

        # Validate configuration at initialization
        validator = WebsiteConfigValidator(self.website_config)
        validator.validate()

    def get_run_config(self) -> CrawlerRunConfig:
        if not self._standard_run_config:
            raise Exception("Standard run config not initialized")
        return self._standard_run_config.clone()

    def get_login_run_config(
        self, full_login_url: str, js_code: list[str], wait_for_condition: str
    ) -> CrawlerRunConfig:
        return CrawlerConfigFactory.create_login_run_config(
            self.get_run_config(), full_login_url, js_code, wait_for_condition
        )

    def _get_search_city(self) -> str:
        """
        Get the search city from filtering configuration.

        Returns:
            str: The city to use for searching. Falls back to "Tilburg" for backwards compatibility.
        """
        if (
            self.filtering_config
            and self.filtering_config.cities
            and len(self.filtering_config.cities) > 0
        ):
            return self.filtering_config.cities[0]
        return "Tilburg"

    @requires_crawler_initialized
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
            log_console=global_config.debug_mode,
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
            raise Exception("Verification failed: We're not on the expected page")

        return True

    @requires_crawler_initialized
    @requires_cookies_accepted
    @requires_login_config
    async def login_async(self) -> bool:
        if self.navigated_to_gallery and not self.login_config.login_required:
            logger.warning(f"Skipping login for {self.website_info.name}")
            return True

        try:
            base_url = self.website_info.base_url
            full_login_url = ""

            if self.login_config.login_url:
                full_login_url = self.login_config.login_url
            else:
                login_url_path = self.login_config.login_url_path
                full_login_url = f"{base_url}{login_url_path}"

            logger.info(
                f"Navigating to login page of {self.website_info.name} and logging in."
            )
            email = os.getenv(self.website_info.name.upper() + "_EMAIL")
            password = os.getenv(self.website_info.name.upper() + "_PASSWORD")

            js_code = [
                f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.login_config.submit_selector}').click();",
            ]

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

            run_config = self.get_login_run_config(
                full_login_url, js_code, wait_for_condition
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
                        f"Navigation in progress detected. Waiting for page to stabilize for {self.website_info.name}."
                    )

                    # Try again with a different wait strategy
                    stabilize_config = CrawlerRunConfig(
                        session_id=self.session_id,
                        cache_mode=CacheMode.BYPASS,
                        js_only=True,
                        wait_for="domcontentloaded",
                        page_timeout=15000,
                        log_console=global_config.debug_mode,
                    )

                    stabilize_result: CrawlResult = await self.crawler.arun(
                        self.current_url or full_login_url, config=stabilize_config
                    )  # type: ignore

                    if stabilize_result.success:
                        logger.info(
                            f"Page stabilized successfully for {self.website_info.name}"
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

    @requires_crawler_initialized
    async def navigate_to_sitemap_async(self) -> str:
        if self.navigated_to_sitemap:
            raise Exception(
                "Already navigated to sitemap. How? Something must be wrong."
            )

        logger.info("Navigating to and extracting sitemap...")
        url = f"{self.website_info.base_url}{self.strategy_config.navigation_config.sitemap}"

        result: CrawlResult = await self.crawler.arun(
            url,
            config=self.get_run_config(),
        )  # type: ignore

        if not result.success:
            raise Exception(f"Failed to navigate to sitemap: {result.error_message}")

        full_sitemap_url = f"{self.website_info.base_url}{self.strategy_config.navigation_config.sitemap}"

        if result.redirected_url == full_sitemap_url or result.url == full_sitemap_url:
            self.navigated_to_sitemap = True
            self.current_url = result.url
            logger.info(f"Navigated to sitemap: {result.url}")
            return result.html
        else:
            self.navigated_to_sitemap = False
            raise Exception(f"Failed to navigate to sitemap: {result.error_message}")

    @requires_crawler_initialized
    @requires_login_config
    async def navigate_to_gallery_async(self, force_navigation: bool = False) -> None:
        """Navigate to the listings/gallery page."""
        if self.navigated_to_gallery and not force_navigation:
            return

        logger.info("Navigating to gallery...")
        url = f"{self.website_info.base_url}{self.strategy_config.navigation_config.gallery}"

        run_config = self.get_run_config()
        result: CrawlResult = await self.crawler.arun(
            url,
            config=run_config,
        )  # type: ignore

        full_login_url = (
            f"{self.website_info.base_url}{self.login_config.login_url_path or ''}"
        )

        if result and result.success and result.redirected_url != full_login_url:
            logger.info(f"Navigating to gallery successful: {result.url}")
            self.navigated_to_gallery = True
            self.current_url = result.url
        else:
            self.current_url = result.redirected_url
            logger.error(f"Navigating to gallery failed: {result.error_message}")
            logger.error(f"Redirected URL: {result.redirected_url}")

    @requires_crawler_initialized
    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.filtering_config:
            logger.info("No filtering configuration provided.")
            return

        search_city = self._get_search_city()
        logger.info(f"Applying filters with search city: {search_city}")

        js = f"""
(async () => {{
    try {{
        const searchContainer = await new Promise((resolve, reject) => {{
            const timeout = 5000;
            const interval = 100;
            const startTime = Date.now();
            
            const check = () => {{
                const element = document.querySelector('.search-default');
                if (element) {{
                    resolve(element);
                    return;
                }}
                
                if (Date.now() - startTime >= timeout) {{
                    reject(new Error('Search container not found within 5s'));
                    return;
                }}
                
                setTimeout(check, interval);
            }};
            
            check();
        }});

        const addressInput = searchContainer.querySelector('.search-field--adres input');
        addressInput.value = '{search_city}';
        
        const searchButton = searchContainer.querySelector('.search-field--button button');
        searchButton.click();
        
    }} catch (error) {{
        console.error('Fout bij zoeken:', error);
    }}
}})();

        """

        run_config = self.get_run_config()
        run_config.js_code = js
        run_config.log_console = True
        run_config.js_only = True
        if self.filtering_config.filters_container_selector:
            run_config.css_selector = self.filtering_config.filters_container_selector

        await self.crawler.arun(
            url=self.current_url,  # type: ignore
            config=run_config,
        )

        logger.info("Applied filters")

    async def extract_sitemap_async(self, sitemap_html: str) -> List[House]:
        regex = self.sitemap_extraction_config.regex
        schema = self.sitemap_extraction_config.schema
        llm_instructions = self.sitemap_extraction_config.extra_llm_instructions

        assert regex is not None
        assert schema is not None

        logger.info(f"Extracting sitemap")
        urls = re.findall(regex, sitemap_html)
        logger.debug(
            "Done with regex. Let's check if it already exists in the database using the urls!"
        )

        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            existing_houses = await house_service.get_houses_by_detail_url_async(urls)
            logger.info(f"Found {len(existing_houses)} existing houses")
            if existing_houses:
                existing_urls = {house.detail_url for house in existing_houses}
                urls = [url for url in urls if url not in existing_urls]

        enable_ui = os.getenv("CRAWLER_ENABLE_UI", "false").lower() == "true"
        dispatcher = SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=enable_ui),
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
            log_console=global_config.debug_mode,
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
                logger.info(f"Extracting data for {result.url}...")

                extracted_data: Optional[Dict[str, Any]] = await llm_service.extract(
                    data_str,
                    schema,
                    extra_instructions=llm_instructions,
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

    @requires_crawler_initialized
    async def extract_gallery_async(self) -> List[House]:
        if not self.navigated_to_gallery:
            raise Exception("Not navigated to gallery")

        logger.info(f"Extracting property listings of {self.website_info.name} step...")
        gallery_extraction_config = (
            self.website_config.strategy_config.gallery_extraction_config
        )
        assert gallery_extraction_config is not None

        assert gallery_extraction_config.correct_urls_paths is not None
        correct_urls = [
            f"{self.website_info.base_url}{path}"
            for path in gallery_extraction_config.correct_urls_paths
        ]

        if not any(correct_url in self.current_url for correct_url in correct_urls):  # type: ignore
            raise Exception(f"Invalid URL: {self.current_url}")

        schema = gallery_extraction_config.schema
        assert schema is not None

        extraction_strategy = None
        if self.gallery_extraction_config.schema_type == SchemaType.XPATH.value:
            extraction_strategy = JsonXPathExtractionStrategy(schema)
        else:
            extraction_strategy = JsonCssExtractionStrategy(schema)

        run_config = self.get_run_config()
        run_config.extraction_strategy = extraction_strategy
        run_config.wait_for = "domcontentloaded"

        if self.gallery_extraction_config.gallery_container_selector:
            run_config.css_selector = (
                self.gallery_extraction_config.gallery_container_selector
            )

        logger.debug(f"Extracting gallery from url: {self.current_url}")
        result: CrawlResult = await self.crawler.arun(url=self.current_url, config=run_config)  # type: ignore

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

    @requires_crawler_initialized
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
            log_console=global_config.debug_mode,
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

        enable_ui = os.getenv("CRAWLER_ENABLE_UI", "false").lower() == "true"
        dispatcher = SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=enable_ui),
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
                url = f"{self.website_info.base_url}{house.detail_url}"
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

    @requires_crawler_initialized
    async def process_details_xpath_css(self, houses: List[House]) -> List[House]:
        logger.info(f"Processing details with xpath/css for {len(houses)} houses...")

        config = self.get_run_config()
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

    @requires_crawler_initialized
    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.cookies_config:
            logger.info("Accepting cookies not required.")
            return True
        if self.accepted_cookies:
            logger.info("Cookies already accepted.")
            return self.accepted_cookies

        logger.info(f"Accepting cookies for {self.website_info.name}...")

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

        cookie_config = self.get_run_config()
        cookie_config.js_only = True
        cookie_config.magic = True
        cookie_config.js_code = js

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
