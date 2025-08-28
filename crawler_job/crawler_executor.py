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


async def _run_single_scraper_with_session(
    website_name: str,
    crawler: AsyncWebCrawler,
    notification_service: NotificationService,
) -> Dict[str, Any]:
    """
    Runs a scraper for a single website using a shared browser instance.
    The session_id is handled by the ScraperFactory from the website config.
    """
    db_session = None
    try:
        # Each scraper gets its own database session
        db_session = get_db_session()
        json_config_repo = JsonConfigRepository(db_session)
        factory = ScraperFactory(json_config_repo, crawler)

        scraper = await factory.get_scraper_async(website_name, notification_service)
        logger.info(f"Starting crawl for website: {website_name}")

        result = await scraper.run_async()

        result.setdefault("total_houses_count", 0)
        result.setdefault("new_houses_count", 0)
        result.setdefault("updated_houses_count", 0)
        result.setdefault("website", website_name)

        return result

    except Exception as e:
        logger.error(f"Error running crawler for {website_name}: {str(e)}")
        return {"success": False, "error": str(e), "website": website_name}
    finally:
        if db_session:
            try:
                await db_session.close()
            except Exception as e:
                logger.warning(
                    f"Error closing database session for {website_name}: {e}"
                )


async def run_crawler_async(
    websites: List[str],
    notifications_enabled: bool,
    test_notifications_only: bool,
    debug_mode: bool,
    headless: bool,
) -> bool:
    notification_service = NotificationService(notifications_on=notifications_enabled)

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

    crawler = AsyncWebCrawler(config=browser_config)
    results: List[Dict[str, Any]] = []

    try:
        await crawler.start()

        tasks = []
        for website_name in websites:
            task = _run_single_scraper_with_session(
                website_name, crawler, notification_service
            )
            tasks.append(task)

        # Execute scrapers in batches with limited concurrency
        # crawl4ai recommends max 2-3 concurrent tasks to avoid resource conflicts
        MAX_CONCURRENT = 3
        all_results = []

        for i in range(0, len(tasks), MAX_CONCURRENT):
            batch = tasks[i : i + MAX_CONCURRENT]
            batch_websites = websites[i : i + MAX_CONCURRENT]

            logger.info(f"Processing batch {i//MAX_CONCURRENT + 1}: {batch_websites}")
            batch_results = await asyncio.gather(*batch, return_exceptions=True)

            for j, result in enumerate(batch_results):
                if isinstance(result, Exception):
                    logger.error(
                        f"Exception in parallel execution for {batch_websites[j]}: {result}"
                    )
                    all_results.append(
                        {
                            "success": False,
                            "error": str(result),
                            "website": batch_websites[j],
                            "total_houses_count": 0,
                            "new_houses_count": 0,
                            "updated_houses_count": 0,
                        }
                    )
                else:
                    if isinstance(result, dict):
                        all_results.append(result)
                    else:
                        logger.error(
                            f"Unexpected result type for {batch_websites[j]}: {type(result)}"
                        )
                        all_results.append(
                            {
                                "success": False,
                                "error": f"Unexpected result type: {type(result)}",
                                "website": batch_websites[j],
                                "total_houses_count": 0,
                                "new_houses_count": 0,
                                "updated_houses_count": 0,
                            }
                        )

    except Exception as e:
        logger.error(f"Error starting crawler: {str(e)}")
        return False
    finally:
        await crawler.close()

    successful_results = [r for r in results if r and r.get("success")]
    success = len(successful_results) == len(websites)

    if results:
        total_houses = sum(r.get("total_houses_count", 0) for r in results if r)
        new_houses = sum(r.get("new_houses_count", 0) for r in results if r)
        updated_houses = sum(r.get("updated_houses_count", 0) for r in results if r)

        logger.info(f"Crawl completed for websites: {', '.join(websites)}")
        logger.info(f"Total houses found: {total_houses}")
        logger.info(f"New houses: {new_houses}")
        logger.info(f"Updated houses: {updated_houses}")
    else:
        logger.error("Crawl failed for all websites. No results to process.")

    if not success:
        failed_websites = [
            r.get("website", "Unknown")
            for r in results
            if not r or not r.get("success")
        ]
        logger.error(f"Crawl failed for websites: {', '.join(failed_websites)}")

    return success
