from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from typing import Optional
from playwright.async_api import Page, BrowserContext
import asyncio
import logging

logger = logging.getLogger(__name__)


async def execute_login_step(
    crawler: AsyncWebCrawler,
    email: str,
    password: str,
    session_id: str,
    max_retries: int = 3,
) -> str:
    expected_url = "https://hurenbij.vesteda.com/"

    run_config = CrawlerRunConfig(
        session_id=session_id,
        cache_mode=CacheMode.BYPASS,
        js_only=True,
        magic=True,
        js_code=[
            "document.querySelector('input[type=\"email\"]').value = '" + email + "';",
            "document.querySelector('input[type=\"password\"]').value = '"
            + password
            + "';",
            "document.querySelector('button[type=\"submit\"]').click();",
        ],
    )

    logger.info("Navigating to login page and logging in.")
    result = await crawler.arun(
        url="https://hurenbij.vesteda.com/login", config=run_config
    )

    if not result.success:
        raise Exception(f"Login form submission failed: {result.error_message}")

    check_config = CrawlerRunConfig(
        session_id=session_id,
        cache_mode=CacheMode.BYPASS,
        js_only=True,
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    )

    # Wait a moment for the redirect to complete
    await asyncio.sleep(2)

    logger.info("Verifying login.")
    check_result = await crawler.arun(
        url="https://hurenbij.vesteda.com/", config=check_config
    )

    if not check_result.success:
        raise Exception(f"Login verification failed: {check_result.error_message}")

    check_result_url = check_result.url
    check_result_redirect_url = check_result.redirected_url

    if check_result_url != expected_url and check_result_redirect_url != expected_url:
        raise Exception(f"Login failed: Still on login page or login elements detected")

    return check_result_url
