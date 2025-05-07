import json
import logging
from typing import AsyncGenerator, Dict, Any, List, Optional
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlResult,
    CrawlerMonitor,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
    DisplayMode,
    JsonCssExtractionStrategy,
    PruningContentFilter,
    RateLimiter,
    SemaphoreDispatcher,
)

from crawler_job.models.house_models import FetchedPage, House
from crawler_job.notifications.notification_service import NotificationService

from ..models.db_config_models import WebsiteConfig
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class VestedaScraper(BaseWebsiteScraper):
    """Vesteda-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        notification_service: Optional[NotificationService] = None,
    ):
        """Initialize the Vesteda scraper.

        Args:
            crawler: The crawl4ai crawler instance to use.
            config: The validated website configuration.
            notification_service: The notification service to use.
        """
        super().__init__(config, session_id, notification_service)

        logger.info(f"Vesteda scraper initialized...")

    def _build_crawler(self) -> AsyncWebCrawler:
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=True,
            use_managed_browser=True,
            user_data_dir="./browser_data/vesteda",
            extra_args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
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

    async def extract_gallery_async(self) -> List[House]:
        if not self.navigated_to_gallery:
            raise Exception("Not navigated to gallery")

        if not self.config.strategy_config.gallery_extraction_config:
            raise Exception("No gallery extraction configuration provided.")

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info("Extracting property listings of Vesteda step...")
        gallery_extraction_config = (
            self.config.strategy_config.gallery_extraction_config
        )

        correct_urls = [
            f"{self.config.base_url}{path}"
            for path in gallery_extraction_config.correct_urls_paths
        ]

        if self.current_url not in correct_urls:
            raise Exception(f"Invalid URL: {self.current_url}")

        schema = gallery_extraction_config.schema

        gallery_config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(schema),
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            magic=False,
            user_agent_mode="random",
        )

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
            # Pre-process the data before passing to from_dict
            processed_data = house_data.copy()

            # Process bedrooms field
            try:
                if "bedrooms" in house_data and house_data["bedrooms"]:
                    processed_data["bedrooms"] = int(house_data["bedrooms"])
            except ValueError:
                logger.warning(
                    f"Could not convert bedrooms to int: {house_data.get('bedrooms')}"
                )
                processed_data["bedrooms"] = None

            # Process area field to square_meters
            try:
                if "area" in house_data and house_data["area"]:
                    # Strip "m²" and convert to int
                    area_str = house_data.get("area", "").replace("m2", "").strip()
                    if area_str:
                        processed_data["square_meters"] = int(area_str)
            except ValueError:
                logger.warning(
                    f"Could not convert area to int: {house_data.get('area')}"
                )
                processed_data["square_meters"] = None

            # Rename price to rental_price
            if "price" in processed_data:
                processed_data["rental_price"] = processed_data.pop("price")

            # Check if demand message indicates high demand
            demand_message = processed_data.get("demand_message")
            high_demand = False
            if demand_message and any(
                keyword in demand_message.lower()
                for keyword in ["hoge interesse", "veel interesse", "popular"]
            ):
                high_demand = True
            processed_data["high_demand"] = high_demand

            # Create House object using from_dict
            house = House.from_dict(processed_data)
            houses.append(house)

        logger.info(f"Successfully extracted {len(houses)} properties")
        return houses

    async def extract_details_async(self, houses: List[House]) -> List[FetchedPage]:
        """
        Extract detailed property information for the given houses

        Args:
            houses: List of House objects with basic info

        Returns:
            List[FetchedPage]: List of fetched detail pages
        """
        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info("Starting detailed property extraction...")

        prune_filter = PruningContentFilter(
            # Lower → more content retained, higher → more content pruned
            threshold=0.45,
            threshold_type="dynamic",
            min_word_threshold=3,
        )
        config = CrawlerRunConfig(
            log_console=False,
            exclude_domains=["deploy.mopinion.com", "app.cobrowser.com"],
            mean_delay=1,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=prune_filter,
            ),
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            js_only=False,
            magic=True,
            user_agent_mode="random",
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
                url = f"{self.config.base_url}{house.detail_url}"
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
            # Return partial results if possible
            return [FetchedPage(url=url, markdown="", success=False) for url in urls]
