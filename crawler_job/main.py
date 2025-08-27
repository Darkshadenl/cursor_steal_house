import asyncio
import argparse
import os
import time
from crawl4ai import AsyncWebCrawler, BrowserConfig
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
from crawler_job.services import config


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
    headless: bool,
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
    db_session = get_db_session()
    notification_service = NotificationService(notifications_on=notifications_enabled)

    try:
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

        # Initialize global configuration
        config.initialize(debug_mode)

        browser_config = BrowserConfig(
            headless=headless,
            verbose=config.debug_mode,
            use_managed_browser=True,
            user_data_dir="./browser_data/general",
            extra_args=[
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--remote-debugging-address=0.0.0.0",
                "--remote-debugging-port=9222",
            ],
        )

        crawler = AsyncWebCrawler(
            config=browser_config,
        )

        json_config_repo = JsonConfigRepository(db_session)
        factory = ScraperFactory(json_config_repo, crawler)
        results: List[Dict[str, Any]] = []

        try:
            await crawler.start()

            logger.info(f"Running for websites: {websites}")

            for website_name in websites:
                scraper = await factory.get_scraper_async(
                    website_name, notification_service
                )

                logger.info(f"Starting crawl for website: {website_name}")
                try:
                    result = await scraper.run_async()
                    results.append(result)
                except Exception as e:
                    logger.error(f"Error running crawler: {str(e)}")

        except Exception as e:
            logger.error(f"Error starting crawler: {str(e)}")
            return False
        finally:
            await crawler.close()

        success = all(result["success"] for result in results)

        if len(results) > 0:
            logger.info(
                f"Crawl completed successfully for websites: {', '.join(websites)}"
            )
            logger.info(
                f"Total houses found: {sum(result['total_houses_count'] for result in results)}"
            )
            logger.info(
                f"New houses: {sum(result['new_houses_count'] for result in results)}"
            )
            logger.info(
                f"Updated houses: {sum(result['updated_houses_count'] for result in results)}"
            )
        else:
            failed_websites = [
                website
                for website in websites
                if not any(result["success"] for result in results)
            ]
            logger.error(
                f"Crawl failed for websites: {', '.join(failed_websites)}. Error: {result.get('error', 'Unknown error')}"
            )

        return success
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
    parser.add_argument(
        "--headless",
        type=str,
        choices=["true", "false"],
        help="Run the browser in headless mode (true/false)",
        default=os.getenv("HEADLESS", "false").lower(),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    websites: List[str] = args.websites
    test_notifications_only: bool = args.test_notifications_only
    notifications_enabled: bool = args.notifications_enabled
    debug_mode: bool = args.debug_mode
    headless: bool = args.headless

    try:
        result = asyncio.run(
            run_crawler_async(
                websites,
                notifications_enabled,
                test_notifications_only,
                debug_mode,
                headless,
            )
        )

        if result:
            sys.exit(0)
        else:
            if config.debug_mode:
                logger.info(
                    "Debug mode enabled - keeping application running after crash"
                )
                while True:
                    time.sleep(10)  # Keep process alive
            else:
                sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Crawl interrupted by user.")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        if config.debug_mode:
            logger.info("Debug mode enabled - keeping application running after crash")
            while True:
                time.sleep(10)  # Keep process alive
        else:
            sys.exit(1)
