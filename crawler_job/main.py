import asyncio
import argparse
import os
import time
from dotenv import load_dotenv
import sys
from typing import List

from crawler_job.services.logger_service import setup_logger
from crawler_job.services import config
from crawler_job.crawler_executor import run_crawler_async


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


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="StealHouse Website Crawler")
    parser.add_argument(
        "--websites",
        type=parse_websites,
        help="Comma-separated list of websites to crawl (e.g., 'Vesteda,Sleutel')",
        default=os.getenv("CRAWLER_WEBSITES", ""),
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
