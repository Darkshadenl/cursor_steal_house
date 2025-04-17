import logging
from typing import List
from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlerMonitor,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
    DisplayMode,
    PruningContentFilter,
    RateLimiter,
    SemaphoreDispatcher,
)
from crawler_job.models.house_models import (
    House,
    FetchedPage,
)

# Configure logging
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


async def execute_detailed_property_extraction(
    crawler: AsyncWebCrawler,
    houses: List[House],
    session_id: str,
) -> List[FetchedPage]:
    """
    Extract detailed property information for the given houses

    Args:
        crawler: The web crawler instance
        houses: List of House objects with basic info
        session_id: The session ID for the crawler

    Returns:
        List[FetchedPage]: List of fetched detail pages
    """
    logger.info("Starting detailed property extraction...")
    main_url = "https://hurenbij.vesteda.com"

    prune_filter = PruningContentFilter(
        # Lower → more content retained, higher → more content pruned
        threshold=0.45,
        threshold_type="dynamic",
        min_word_threshold=3,
    )
    config = CrawlerRunConfig(
        log_console=False,
        exclude_domains=["deploy.mopinion.com", "app.cobrowser.com"],
        mean_delay=1,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=prune_filter,
        ),
        cache_mode=CacheMode.BYPASS,
        session_id=session_id,
        js_only=False,
        magic=False,
        user_agent_mode="random",
    )

    dispatcher = SemaphoreDispatcher(
        semaphore_count=1,
        max_session_permit=1,
        monitor=CrawlerMonitor(max_visible_rows=10, display_mode=DisplayMode.DETAILED),
        rate_limiter=RateLimiter(
            base_delay=(3.0, 5.0),
            max_delay=30.0,
            max_retries=3,
            rate_limit_codes=[429, 503],
        ),
    )

    urls = []
    for house in houses:
        if house.detail_url:
            url = main_url + house.detail_url
            urls.append(url)

    logger.info(f"Starting fetch for {len(urls)} properties...")

    try:
        results = await crawler.arun_many(
            urls=urls, config=config, dispatcher=dispatcher
        )

        fetched_pages = []
        for result in results:
            if result.success:
                fetched_pages.append(
                    FetchedPage(
                        url=result.url,
                        markdown=result.markdown.raw_markdown,
                        success=True,
                    )
                )
            else:
                error_msg = (
                    result.error_message
                    if hasattr(result, "error_message")
                    else "Unknown error"
                )
                logger.error(f"{RED}Error fetching property: {error_msg}{RESET}")
                fetched_pages.append(
                    FetchedPage(url=result.url, markdown="", success=False)
                )

        logger.info(
            f"{GREEN}Completed fetching property pages. Successfully fetched {sum(1 for page in fetched_pages if page.success)} out of {len(urls)} properties.{RESET}"
        )
        return fetched_pages
    except Exception as e:
        logger.error(
            f"{RED}Critical error during detailed property extraction: {str(e)}{RESET}"
        )
        # Return partial results if possible
        return [FetchedPage(url=url, markdown="", success=False) for url in urls]
