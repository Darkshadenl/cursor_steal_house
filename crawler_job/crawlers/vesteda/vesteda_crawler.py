import asyncio
import os
import logging
from crawl4ai import AsyncWebCrawler, BrowserConfig
from dotenv import load_dotenv

from .vesteda_steps import (
    execute_detailed_property_extraction,
    execute_login_step,
    execute_search_navigation,
    execute_property_extraction,
    accept_cookies,
    execute_llm_extraction,
)
from crawler_job.services.house_service import HouseService
from crawler_job.models.house_models import (
    DetailHouse,
    FetchedPage,
    GalleryHouse,
)
from crawler_job.services.llm_service import LLMProvider
from crawler_job.notifications.notification_service import NotificationService
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("vesteda_crawler.log")],
)
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

load_dotenv()


class VestedaCrawler:
    def __init__(self):
        # Get verbose setting from environment variable, default to False
        verbose = os.getenv("CRAWLER_VERBOSE", "False").lower() == "true"
        logger.info(f"Browser verbose mode: {verbose}")

        self.browser_config = BrowserConfig(
            headless=True,
            verbose=verbose,
            use_managed_browser=True,
            user_data_dir="./browser_data/vesteda",
        )
        self.base_url = "https://hurenbij.vesteda.com"
        self.email = os.getenv("VESTEDA_EMAIL")
        self.password = os.getenv("VESTEDA_PASSWORD")
        self.session_id = "vesteda_session"
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")

        # Initialize notification service after loading environment variables
        self.notification_service = NotificationService()

    async def run_full_crawl(self) -> Dict[str, Any]:
        """Run a full crawl of Vesteda website and store results in database"""
        try:
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                # Navigate to search page
                url = await execute_search_navigation(crawler, self.session_id)

                # Handle login if needed
                if url == "https://hurenbij.vesteda.com/login/":
                    logger.info("Login required. Accepting cookies and logging in...")
                    await accept_cookies(crawler, url, self.session_id)
                    await execute_login_step(
                        crawler, self.email, self.password, self.session_id
                    )
                    url = await execute_search_navigation(crawler, self.session_id)

                # Extract property listing
                gallery_data: List[GalleryHouse] = await execute_property_extraction(
                    crawler, url, self.session_id
                )

                # Deferred storage until after detail extraction
                detail_houses: List[DetailHouse] = []
                fetched_pages: List[FetchedPage] = []

                # Initialize HouseService with notification service
                async with HouseService(
                    notification_service=self.notification_service
                ) as house_service:
                    # Only process new houses
                    new_houses = await house_service.identify_new_houses(gallery_data)

                    if new_houses:
                        logger.info(
                            f"Fetching details for {len(new_houses)} new houses..."
                        )
                        fetched_pages = await execute_detailed_property_extraction(
                            crawler, new_houses, self.session_id
                        )

                        # Extract structured data using LLM
                        detail_houses = await execute_llm_extraction(
                            fetched_pages, provider=LLMProvider.GEMINI
                        )

                    # Atomic transaction for all database operations
                    result = await house_service.store_houses_atomic(
                        gallery_houses=gallery_data,
                        detail_houses=detail_houses,
                        all_houses=gallery_data,  # Pass the original gallery data
                    )

                return {
                    "gallery_count": len(gallery_data),
                    "new_houses_count": result["new_count"],
                    "existing_houses_count": result["existing_count"],
                    "detail_count": len(detail_houses),
                    "success": True,
                }

        except Exception as e:
            logger.error(f"{RED}Error during crawl: {str(e)}{RESET}")
            raise e

    async def test_notifications_only(self) -> Dict[str, Any]:
        """Run only the test notification functionality without crawling"""
        try:
            logger.info(
                f"{YELLOW}Sending test notification to all active channels...{RESET}"
            )
            successful_channels = (
                await self.notification_service.send_test_notification()
            )

            if successful_channels:
                logger.info(
                    f"{GREEN}Test notifications sent successfully to: {', '.join(successful_channels)}{RESET}"
                )
            else:
                logger.warning(
                    f"{YELLOW}No test notifications were sent successfully. Please check your configuration.{RESET}"
                )

            return {
                "success": len(successful_channels) > 0,
                "successful_channels": successful_channels,
            }

        except Exception as e:
            logger.error(f"{RED}Error sending test notifications: {str(e)}{RESET}")
            return {"success": False, "error": str(e)}


if __name__ == "__main__":
    crawler = VestedaCrawler()
    try:
        print(os.getenv("NOTIFICATION_CHANNELS_ACTIVE"))
        
        
        logger.info("Starting vesteda crawl...")

        # If TEST_NOTIFICATIONS_ONLY is set, only run test notifications
        if os.getenv("TEST_NOTIFICATIONS_ONLY", "false").lower() == "true":
            logger.info(f"{YELLOW}Running in test notifications only mode{RESET}")
            result = asyncio.run(crawler.test_notifications_only())
        else:
            result = asyncio.run(crawler.run_full_crawl())

        logger.info(f"{GREEN}Crawl completed successfully!{RESET}")
    except Exception as e:
        logger.error(f"{RED}Error during crawl: {str(e)}{RESET}")
        raise e
