import asyncio
import argparse
import logging
import os
from dotenv import load_dotenv
import sys
from typing import Dict, Any

from crawler_job.services.db_connection import get_db_session
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.factories import ScraperFactory
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("steal_house_crawler.log"),
    ],
)
logger = logging.getLogger(__name__)

# ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

load_dotenv()


async def run_crawler_async(
    website_name: str, test_notifications_only: bool
) -> Dict[str, Any]:
    """
    Run the crawler for the specified website.

    Args:
        website_name: Name of the website to crawl
        test_notifications_only: If True, only send test notifications without crawling

    Returns:
        Dict[str, Any]: Results of the crawling process
    """
    try:
        db_session = get_db_session()
        notification_service = NotificationService(
            notifications_on=not test_notifications_only
        )

        if test_notifications_only:
            logger.info(f"{YELLOW}Running in test notifications only mode{RESET}")
            successful_channels = await notification_service.send_test_notification()

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

        json_config_repo = JsonConfigRepository(db_session)
        factory = ScraperFactory(json_config_repo)

        scraper = await factory.get_scraper_async(website_name)

        logger.info(f"Starting crawl for website: {website_name}")
        result = await scraper.run_async()

        return {"success": True, "result": "hi"}
        # Log results
        # if result["success"]:
        #     logger.info(
        #         f"{GREEN}Crawl completed successfully for website: {website_name}{RESET}"
        #     )
        #     logger.info(f"Total houses found: {result['total_houses_count']}")
        #     logger.info(f"New houses: {result['new_houses_count']}")
        #     logger.info(f"Existing houses: {result['existing_houses_count']}")
        #     logger.info(f"Updated houses: {result['updated_houses_count']}")
        # else:
        #     logger.error(
        #         f"{RED}Crawl failed for website: {website_name}. Error: {result.get('error', 'Unknown error')}{RESET}"
        #     )

        # return result

    except Exception as e:
        logger.error(f"{RED}Error running crawler: {str(e)}{RESET}")
        return {"success": False, "error": str(e)}
    finally:
        # Close DB session
        if "db_session" in locals():
            await db_session.close()

        # Close browser if scraper was created
        if "scraper" in locals() and hasattr(scraper, "crawler"):
            await scraper.crawler.close()


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="StealHouse Website Crawler")
    parser.add_argument(
        "--website",
        type=str,
        help="Name of the website to crawl (e.g., 'Vesteda')",
        default=os.getenv("CRAWLER_WEBSITE", "Vesteda"),
    )
    parser.add_argument(
        "--test-notifications-only",
        action="store_true",
        help="Only send test notifications without crawling",
        default=os.getenv("TEST_NOTIFICATIONS_ONLY", "false").lower() == "true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()
    website_name = args.website
    test_notifications_only = args.test_notifications_only

    try:
        # Run the crawler
        result = asyncio.run(run_crawler_async(website_name, test_notifications_only))

        # Exit with appropriate code
        sys.exit(0 if result.get("success", False) else 1)
    except KeyboardInterrupt:
        logger.info(f"{YELLOW}Crawl interrupted by user.{RESET}")
        sys.exit(130)
    except Exception as e:
        logger.error(f"{RED}Unhandled exception: {str(e)}{RESET}")
        sys.exit(1)
