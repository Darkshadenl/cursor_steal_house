import asyncio
import argparse
import os
from dotenv import load_dotenv
import sys
from typing import Dict, Any, List

from crawler_job.services.db_connection import get_db_session
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger
from crawler_job.factories import ScraperFactory
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)


logger = setup_logger(__name__)

load_dotenv()


def parse_websites(arg: str) -> List[str]:
    """
    Parse a comma-separated string of website names into a list.

    Args:
        arg: Comma-separated string of website names

    Returns:
        List of website names
    """
    return [website.strip() for website in arg.split(",")]


async def run_crawler_async(
    websites: List[str],
    notifications_enabled: bool,
    test_notifications_only: bool,
    debug_mode: bool,
) -> bool:
    """
    Run the crawler for the specified website.

    Args:
        websites: List of website names to crawl
        notifications_enabled: Whether notifications are enabled
        test_notifications_only: If True, only send test notifications without crawling

    Returns:
        Dict[str, Any]: Results of the crawling process
    """
    try:
        db_session = get_db_session()
        notification_service = NotificationService(
            notifications_on=notifications_enabled
        )

        if test_notifications_only:
            logger.info("Running in test notifications only mode")
            successful_channels = await notification_service.send_test_notification()

            if successful_channels:
                logger.info(
                    f"Test notifications sent successfully to: {', '.join(successful_channels)}"
                )
            else:
                logger.warning(
                    "No test notifications were sent successfully. Please check your configuration."
                )

            return True

        json_config_repo = JsonConfigRepository(db_session)
        factory = ScraperFactory(json_config_repo, debug_mode)
        results: List[Dict[str, Any]] = []

        for website_name in websites:
            # if website_name == "vesteda":
            #     continue

            scraper = await factory.get_scraper_async(
                website_name, notification_service
            )

            logger.info(f"Starting crawl for website: {website_name}")
            try:
                
                result = await scraper.run_async()
                results.append(result)
                if result["success"]:
                    logger.info(f"Crawl completed successfully for website: {website_name}")
                    logger.info(f"Total houses found: {result['total_houses_count']}")
                    logger.info(f"New houses: {result['new_houses_count']}")
                    logger.info(f"Updated houses: {result['updated_houses_count']}")
                else:
                    logger.error(
                        f"Crawl failed for website: {website_name}. Error: {result.get('error', 'Unknown error')}"
                    )
            except Exception as e:
                logger.error(f"Error running crawler: {str(e)}")

        success = all(result["success"] for result in results)

        return success

    except Exception as e:
        logger.error(f"Error running crawler: {str(e)}")
        return False
    finally:
        if "db_session" in locals():
            await db_session.close()


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="StealHouse Website Crawler")
    parser.add_argument(
        "--websites",
        type=parse_websites,
        help="Comma-separated list of websites to crawl (e.g., 'Vesteda,Sleutel')",
        default=os.getenv("CRAWLER_WEBSITES", "Vesteda"),
    )
    parser.add_argument(
        "--notifications-enabled",
        action="store_true",
        help="Enable notifications",
        default=os.getenv("NOTIFICATIONS_ENABLED", "false").lower() == "true",
    )
    parser.add_argument(
        "--test-notifications-only",
        action="store_true",
        help="Only send test notifications without crawling",
        default=os.getenv("TEST_NOTIFICATIONS_ONLY", "false").lower() == "true",
    )
    parser.add_argument(
        "--debug-mode",
        action="store_true",
        help="Enable debug mode",
        default=os.getenv("DEBUG_MODE", "false").lower() == "true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    websites: List[str] = args.websites
    test_notifications_only: bool = args.test_notifications_only
    notifications_enabled: bool = args.notifications_enabled
    debug_mode: bool = args.debug_mode
    try:
        result = asyncio.run(
            run_crawler_async(
                websites,
                notifications_enabled,
                test_notifications_only,
                debug_mode,
            )
        )

        sys.exit(0 if result else 1)
    except KeyboardInterrupt:
        logger.info("Crawl interrupted by user.")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        sys.exit(1)
