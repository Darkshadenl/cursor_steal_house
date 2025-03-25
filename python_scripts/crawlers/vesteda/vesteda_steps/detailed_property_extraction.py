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
from python_scripts.crawlers.vesteda.vesteda_models.house_models import (
    GalleryHouse,
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
    crawler: AsyncWebCrawler, data: List[GalleryHouse], session_id: str
) -> List[FetchedPage]:
    logger.info("Starting detailed property extraction (two-step process)...")
    main_url = "https://hurenbij.vesteda.com"

    prune_filter = PruningContentFilter(
        # Lower → more content retained, higher → more content pruned
        threshold=0.45,
        threshold_type="dynamic",
        min_word_threshold=3,
    )
    config = CrawlerRunConfig(
        log_console=True,
        markdown_generator=DefaultMarkdownGenerator(content_filter=prune_filter),
        cache_mode=CacheMode.ENABLED,
        session_id=session_id,
        js_only=False,
        magic=False,
    )

    dispatcher = SemaphoreDispatcher(
        semaphore_count=3,
        max_session_permit=3,
        monitor=CrawlerMonitor(max_visible_rows=10, display_mode=DisplayMode.DETAILED),
        rate_limiter=RateLimiter(
            base_delay=(2.0, 4.0),
            max_delay=30.0,
            max_retries=3,
            rate_limit_codes=[429, 503],
        ),
    )

    urls = []
    for house in data:
        url = main_url + house.detail_url
        urls.append(url)

    logger.info(f"Starting fetch for {len(urls)} properties...")

    results = await crawler.arun_many(urls=urls, config=config, dispatcher=dispatcher)

    fetched_pages = []
    for result in results:
        if result.success:
            fetched_pages.append(
                FetchedPage(
                    url=result.url, markdown=result.markdown.raw_markdown, success=True
                )
            )
        else:
            logger.error(f"{RED}Error fetching property: {result.error_message}{RESET}")
            fetched_pages.append(
                FetchedPage(url=result.url, markdown="", success=False)
            )

    logger.info(
        f"{GREEN}Completed fetching property pages. Successfully fetched {sum(1 for page in fetched_pages if page.success)} out of {len(urls)} properties.{RESET}"
    )

    return fetched_pages
