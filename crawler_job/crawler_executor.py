import asyncio
import os
from typing import Dict, Any, List, Optional
from crawl4ai import BrowserConfig

from crawler_job.crawl4ai_wrappers.CustomAsyncWebCrawler import CustomAsyncWebCrawler
from crawler_job.services.db_connection import get_db_session
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger
from crawler_job.factories import ScraperFactory
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)
from crawler_job.services.config_provider import ConfigProviderFactory
from crawler_job.services import config


logger = setup_logger(__name__)


def _create_browser_config(website_name: str, headless: bool) -> BrowserConfig:
    return BrowserConfig(
        headless=headless,
        verbose=config.debug_mode,
        use_managed_browser=False,
        user_data_dir=f"./browser_data/{website_name}",
        extra_args=[
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
        ],
    )


def _setup_notifications(notifications_enabled: bool) -> NotificationService:
    return NotificationService(notifications_on=notifications_enabled)


async def _run_single_scraper_with_session(
    website_name: str,
    crawler: CustomAsyncWebCrawler,
    notification_service: NotificationService,
) -> Dict[str, Any]:
    db_session = None
    json_config_repo: Optional[JsonConfigRepository] = None
    try:
        if config.config_source == "db":
            db_session = get_db_session()
            json_config_repo = JsonConfigRepository(db_session)

        config_provider = ConfigProviderFactory.create_provider(
            config.config_source, json_config_repository=json_config_repo
        )
        factory = ScraperFactory(config_provider, crawler)

        scraper = await factory.get_scraper_async(website_name, notification_service)
        logger.info(f"Starting crawl for website: {website_name}")

        from crawler_job.helpers.strategy_executor import StrategyExecutor

        result = await StrategyExecutor(scraper).run_scraper()

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


async def _execute_scrapers_concurrent_async(
    websites: List[str],
    crawlers: List[CustomAsyncWebCrawler],
    notification_service: NotificationService,
    max_concurrent: int = 3,
) -> List[Dict[str, Any]]:
    tasks = []
    for i, website_name in enumerate(websites):
        task = _run_single_scraper_with_session(
            website_name, crawlers[i], notification_service
        )
        tasks.append(task)

    all_results = []
    for i in range(0, len(tasks), max_concurrent):
        batch = tasks[i : i + max_concurrent]
        batch_websites = websites[i : i + max_concurrent]

        logger.info(f"Processing batch {i//max_concurrent + 1}: {batch_websites}")
        batch_results = await asyncio.gather(*batch, return_exceptions=True)

        for j, result in enumerate(batch_results):
            if isinstance(result, Exception):
                logger.error(
                    f"Exception in concurrent execution for {batch_websites[j]}: {result}"
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

    return all_results


async def _execute_scrapers_sequential_async(
    websites: List[str],
    crawlers: List[CustomAsyncWebCrawler],
    notification_service: NotificationService,
) -> List[Dict[str, Any]]:
    results = []
    for i, website_name in enumerate(websites):
        logger.info(f"Processing website {i + 1}/{len(websites)}: {website_name}")
        result = await _run_single_scraper_with_session(
            website_name, crawlers[i], notification_service
        )
        results.append(result)

    return results


def _log_results(results: List[Dict[str, Any]], websites: List[str]) -> bool:
    successful_results = [r for r in results if r and r.get("success")]
    success = len(successful_results) == len(websites)

    if success:
        total_houses = sum(r.get("total_houses_count", 0) for r in results if r)
        new_houses = sum(r.get("new_houses_count", 0) for r in results if r)
        updated_houses = sum(r.get("updated_houses_count", 0) for r in results if r)

        logger.info(f"Crawl completed for websites: {', '.join(websites)}")
        logger.info(f"Total houses found: {total_houses}")
        logger.info(f"New houses: {new_houses}")
        logger.info(f"Updated houses: {updated_houses}")
    else:
        logger.error("Crawl failed for all websites. No results to process.")
        failed_websites = [
            r.get("website", "Unknown")
            for r in results
            if not r or not r.get("success")
        ]
        logger.error(f"Crawl failed for websites: {', '.join(failed_websites)}")

    return success


async def run_crawler_async(
    websites: List[str],
    notifications_enabled: bool,
    test_notifications_only: bool,
    debug_mode: bool,
    headless: bool,
) -> bool:
    notification_service = _setup_notifications(notifications_enabled)

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

    concurrent_scrapers = os.getenv("CONCURRENT_SCRAPERS", "true").lower() == "true"
    max_concurrent = int(os.getenv("MAX_CONCURRENT_SCRAPERS", "3"))

    crawlers: List[CustomAsyncWebCrawler] = []

    try:
        for website_name in websites:
            browser_config = _create_browser_config(website_name, headless)
            crawler = CustomAsyncWebCrawler(config=browser_config)
            await crawler.start()
            crawlers.append(crawler)

        if concurrent_scrapers:
            logger.info(
                f"Running scrapers concurrently (max {max_concurrent} at a time)"
            )
            results = await _execute_scrapers_concurrent_async(
                websites, crawlers, notification_service, max_concurrent
            )
        else:
            logger.info("Running scrapers sequentially")
            results = await _execute_scrapers_sequential_async(
                websites, crawlers, notification_service
            )

    except Exception as e:
        logger.error(f"Error starting crawler: {str(e)}")
        return False
    finally:
        for crawler in crawlers:
            try:
                await crawler.close()
            except Exception as e:
                logger.warning(f"Error closing crawler: {e}")

    return _log_results(results, websites)
