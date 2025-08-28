import asyncio
from typing import Dict, Any, List
from crawl4ai import AsyncWebCrawler, BrowserConfig

from crawler_job.services.db_connection import get_db_session
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger
from crawler_job.factories import ScraperFactory
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)
from crawler_job.services import config


logger = setup_logger(__name__)


async def run_crawler_async(
    websites: List[str],
    notifications_enabled: bool,
    test_notifications_only: bool,
    debug_mode: bool,
    headless: bool,
) -> bool:
    """
    Run the crawler for the specified websites.

    Args:
        websites: List of website names to crawl
        notifications_enabled: Whether notifications are enabled
        test_notifications_only: If True, only send test notifications without crawling
        debug_mode: Whether debug mode is enabled
        headless: Whether to run browser in headless mode

    Returns:
        bool: True if all crawls succeeded, False otherwise
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
                    logger.error(f"Error running crawler for {website_name}: {str(e)}")

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
                f"Crawl failed for websites: {', '.join(failed_websites)}. Error: {result.get('error', 'Unknown error') if results else 'No results'}"
            )

        return success
    finally:
        if "db_session" in locals():
            await db_session.close()
