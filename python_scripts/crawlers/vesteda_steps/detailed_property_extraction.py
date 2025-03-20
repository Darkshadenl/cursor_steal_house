import json
import logging
from typing import List
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerMonitor, CrawlerRunConfig, DefaultMarkdownGenerator, DisplayMode, LLMConfig, LLMExtractionStrategy, MemoryAdaptiveDispatcher, PruningContentFilter, RateLimiter, SemaphoreDispatcher

from python_scripts.crawlers.vesteda_models.house_models import DetailHouse, GalleryHouse

# Configure logging
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

async def execute_detailed_property_extraction(crawler: AsyncWebCrawler, data: List[GalleryHouse], session_id: str, deepseek_api_key: str) -> List[DetailHouse]:
    logger.info("Starting detailed property extraction...")
    prune_filter = PruningContentFilter(
        threshold=0.4,
        threshold_type="dynamic",  # or "dynamic"
    )
    markdown_generator = DefaultMarkdownGenerator(
            content_filter=prune_filter,
    )
     
    llm_config = LLMExtractionStrategy(
        llm_config=LLMConfig(
            provider="deepseek/deepseek-chat",
            api_token=deepseek_api_key
            ),
        js_on=True,
        schema={"type": "array", "items": DetailHouse.model_json_schema()},
        extraction_type="schema",
        input_format="fit_markdown",
        instruction="""
        A markdown text will be provided with information about a house.
        Extract all house data displayed in this markdown text.
        """,
        extra_args={"temperature": 0.1}
    )
    
    config = CrawlerRunConfig(
        markdown_generator=markdown_generator,
        extraction_strategy=llm_config,
        cache_mode=CacheMode.BYPASS,
        session_id=session_id
    )
    
    dispatcher = SemaphoreDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=5,  # Maximum concurrent tasks
        monitor=CrawlerMonitor(
        # Maximum rows in live display
        max_visible_rows=20,          

        # DETAILED or AGGREGATED view
        display_mode=DisplayMode.DETAILED  
    ),
        rate_limiter=RateLimiter(
        base_delay=(2.0, 4.0),  # Random delay between 2-4 seconds
        max_delay=30.0,         # Cap delay at 30 seconds
        max_retries=3,          # Retry up to 5 times on rate-limiting errors
        rate_limit_codes=[429, 503]  # Handle these HTTP status codes
    )
    )

    list_of_house_details = []
    urls = []
    
    for house in data:
        url = house['detail_url']
        urls.append(url)
    
    logger.info(f"Starting extraction for {len(urls)} properties...")
        
    results = await crawler.arun_many(
            urls=urls,
            config=config,
            dispatcher=dispatcher
        )
        
    for result in results:
        if result.success:
            house_detail_data = json.loads(result.extracted_content)
            llm_config.show_usage()  #prints token usage
            logger.info(f"{GREEN}Successfully extracted house: {house_detail_data['address']}{RESET}")
            list_of_house_details.append(house_detail_data)
        else:
            logger.error(f"{RED}Error extracting property: {result.error_message}{RESET}")
    
    logger.info(f"{GREEN}Completed detailed property extraction. Successfully extracted {len(list_of_house_details)} out of {len(urls)} properties.{RESET}")
    return list_of_house_details
    