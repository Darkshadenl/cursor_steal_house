import os
import json
from typing import List, Optional
from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlResult,
    CrawlerRunConfig,
    JsonCssExtractionStrategy,
    SemaphoreDispatcher,
)

from crawler_job.crawl4ai_wrappers.CustomAsyncWebCrawler import CustomAsyncWebCrawler
from crawler_job.models.house_models import House
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.data_processing_service import DataProcessingService
from crawler_job.services.llm_extraction_service import LlmExtractionService

from ..models.pydantic_models import WebsiteScrapeConfigJson
from .base_scraper import BaseWebsiteScraper
from crawler_job.services.logger_service import setup_logger
from crawler_job.helpers.decorators import (
    requires_crawler_initialized,
    requires_navigated_to_gallery,
)
from crawler_job.services import config as global_config

logger = setup_logger(__name__)


class VestedaScraper(BaseWebsiteScraper):
    """Vesteda-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteScrapeConfigJson,
        session_id: str,
        crawler: CustomAsyncWebCrawler,
        standard_run_config: CrawlerRunConfig,
        standard_dispatcher: SemaphoreDispatcher,
        data_processing_service: DataProcessingService,
        llm_extraction_service: LlmExtractionService,
        notification_service: Optional[NotificationService] = None,
    ):
        super().__init__(
            config=config,
            session_id=session_id,
            crawler=crawler,
            standard_run_config=standard_run_config,
            standard_dispatcher=standard_dispatcher,
            data_processing_service=data_processing_service,
            llm_extraction_service=llm_extraction_service,
            notification_service=notification_service,
        )

        logger.debug("Vesteda scraper initialized...")

    def _create_login_verification_hook_async(self):
        async def verify_login_hook(page, context, url="", response=None, **kwargs):
            result = await page.evaluate(
                """() => {
                const storageKey = '5da451d1e48514.00659317_bre';
                const storageData = localStorage.getItem(storageKey);
                
                if (!storageData) {
                    return {
                        success: false,
                        error: `localStorage key '${storageKey}' not found`,
                        allKeys: Object.keys(localStorage)
                    };
                }
                
                try {
                    const data = JSON.parse(storageData);
                    const previousPage = data?.v?.previous_page || '';
                    const currentPage = data?.v?.current_page || '';
                    
                    const isFromLogin = previousPage.includes('/login/');
                    const isLoggedIn = currentPage.includes('hurenbij.vesteda.com') && 
                                      !currentPage.includes('/login/');
                    
                    return {
                        success: isFromLogin && isLoggedIn,
                        previousPage: previousPage,
                        currentPage: currentPage,
                        storageData: data
                    };
                } catch (e) {
                    return {
                        success: false,
                        error: `Failed to parse localStorage data: ${e.message}`,
                        rawData: storageData
                    };
                }
            }"""
            )

            if "not found" in result.get("error", ""):
                logger.debug("localStorage key not yet created, continuing...")
                return page

            if not result.get("success"):
                current = result.get("currentPage", "")
                previous = result.get("previousPage", "")

                if "/login" in current and (not previous or "/login" in previous):
                    logger.debug(
                        f"Login in progress - current at login page (previous: '{previous}')"
                    )
                    return page

                error_msg = result.get("error", "Unknown error")
                logger.error(f"Vesteda login verification failed: {error_msg}")
                raise Exception(
                    f"Vesteda login verification failed: {error_msg}. "
                    f"Result: {result}"
                )

            logger.info(
                f"✅ Vesteda login verified - previous: {result.get('previousPage')}, "
                f"current: {result.get('currentPage')}"
            )
            return page

        return verify_login_hook

    @requires_crawler_initialized
    @requires_navigated_to_gallery
    async def extract_gallery_async(self) -> List[House]:
        logger.info("Extracting property listings of Vesteda step...")
        assert self.gallery_extraction_config is not None
        schema = self.gallery_extraction_config.schema
        assert schema is not None

        gallery_config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(schema),
            cache_mode=CacheMode.BYPASS,
            session_id=self.session_id,
            magic=False,
            user_agent_mode="random",
            log_console=global_config.debug_mode,
            exclude_all_images=True,
            exclude_social_media_links=True,
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
            house.detail_url = f"{self.website_info.base_url}{house.detail_url}"
            houses.append(house)

        logger.info(f"Successfully extracted {len(houses)} properties")
        return houses
