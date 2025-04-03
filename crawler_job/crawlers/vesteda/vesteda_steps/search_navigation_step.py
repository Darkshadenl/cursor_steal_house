from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from typing import Optional, Dict
from .cookie_acceptor import accept_cookies


async def execute_search_navigation(crawler: AsyncWebCrawler, session_id: str) -> str:
    run_config = CrawlerRunConfig(
        session_id=session_id,
        cache_mode=CacheMode.BYPASS,
        magic=True,
    )

    result = await crawler.arun(
        url="https://hurenbij.vesteda.com/zoekopdracht/", config=run_config
    )

    if (
        result
        and result.success
        and result.redirected_url != "https://hurenbij.vesteda.com/login/"
    ):
        print(f"Search navigation successful: {result.url}")
        return result.url
    else:
        print(f"Search navigation failed: {result.error_message}")
        print(f"Redirected URL: {result.redirected_url}")
        return result.redirected_url
