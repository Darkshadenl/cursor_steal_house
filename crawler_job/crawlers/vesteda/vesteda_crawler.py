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
    House,
)
from crawler_job.services.llm_service import LLMProvider
from crawler_job.notifications.notification_service import NotificationService
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("vesteda_crawler.log")],
)
logger = logging.getLogger(__name__)

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

load_dotenv()


class VestedaCrawler:
    def __init__(
        self,
        verbose: bool = False,
        test_notifications_only: bool = False,
        notifications_on: bool = False,
    ):
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

        self.notification_service = NotificationService(notifications_on)

        try:
            logger.info("Starting vesteda crawl...")

            if test_notifications_only == True:
                logger.info(f"{YELLOW}Running in test notifications only mode{RESET}")
                asyncio.run(self.test_notifications_only())
            else:
                asyncio.run(self.run_full_crawl())

            logger.info(f"{GREEN}Crawl completed successfully!{RESET}")
        except Exception as e:
            logger.error(f"{RED}Error during crawl: {str(e)}{RESET}")
            raise e

    async def run_full_crawl(self):
        """
        Run a full crawl of Vesteda website and store results in database

        Returns:
            Dict[str, Any]: Dictionary with crawl statistics
        """
        try:
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                url = await execute_search_navigation(crawler, self.session_id)

                if url == "https://hurenbij.vesteda.com/login":
                    logger.info("Login required. Accepting cookies and logging in...")
                    await accept_cookies(crawler, url, self.session_id)
                    await execute_login_step(
                        crawler, self.email, self.password, self.session_id
                    )
                    url = await execute_search_navigation(crawler, self.session_id)

                houses: List[House] = await execute_property_extraction(
                    crawler, url, self.session_id
                )
                logger.info(f"Found {len(houses)} houses on the page")

            async with HouseService(
                notification_service=self.notification_service
            ) as house_service:
                new_houses = await house_service.identify_new_houses_async(houses)

                if not new_houses:
                    logger.info("No new houses found. Exiting...")
                    return

                logger.info(f"Fetching details for {len(new_houses)} new houses...")

                async with AsyncWebCrawler(config=self.browser_config) as crawler:
                    # Fetch detailed pages for new houses
                    fetched_pages = await execute_detailed_property_extraction(
                        crawler, new_houses, self.session_id
                    )

                # Extract detailed data using LLM and update house objects
                detailed_houses = await execute_llm_extraction(
                    fetched_pages, provider=LLMProvider.GEMINI
                )

                if not detailed_houses:
                    logger.info("No detailed houses found. Exiting...")
                    return

                logger.info(f"Merging details for {len(detailed_houses)} houses...")
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

                await house_service.store_houses_atomic_async(
                    houses=houses,
                    all_houses=houses,
                )

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
