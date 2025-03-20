import json
import logging
from typing import List
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerMonitor, CrawlerRunConfig, DefaultMarkdownGenerator, DisplayMode, JsonCssExtractionStrategy, JsonXPathExtractionStrategy, LLMConfig, LLMExtractionStrategy, MemoryAdaptiveDispatcher, PruningContentFilter, RateLimiter, SemaphoreDispatcher

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
    main_url = 'https://hurenbij.vesteda.com'
    
    prune_filter = PruningContentFilter(
        threshold=0.4,
        threshold_type="dynamic",  # or "dynamic"
    )
    markdown_generator = DefaultMarkdownGenerator(
            content_filter=prune_filter,
    )
    
    configA = CrawlerRunConfig(
        
        cache_mode=CacheMode.BYPASS,
        session_id=session_id
    )
    # resultA = await crawler.arun(main_url + data[0]['detail_url'], configA)
    
    # schema_xpath = JsonCssExtractionStrategy.generate_schema(
    #     resultA.cleaned_html,
    #     schema_type="xpath",
    #     llm_config = LLMConfig(provider="deepseek/deepseek-chat",api_token=deepseek_api_key)
    # )
    
    # llm_config = LLMExtractionStrategy(
    #     llm_config=LLMConfig(
    #         provider="deepseek/deepseek-chat",
    #         api_token=deepseek_api_key
    #         ),
    #     js_on=True,
    #     schema={"type": "array", "items": DetailHouse.model_json_schema()},
    #     extraction_type="schema",
    #     input_format="fit_markdown",
    #     instruction="""
    #     A markdown text will be provided with information about a house.
    #     Extract all house data displayed in this markdown text.
    #     """,
    #     extra_args={"temperature": 0.1}
    # )
    
    # Load the JSON schema for property details
    with open("python_scripts/crawlers/vesteda_steps/detailed_property_schema.json", "r") as f:
        schema = json.load(f)
    
    schema_xpath = JsonXPathExtractionStrategy(schema=schema, verbose=True)
    
    config = CrawlerRunConfig(
        markdown_generator=markdown_generator,
        extraction_strategy=schema_xpath,
        cache_mode=CacheMode.BYPASS,
        session_id=session_id
    )

    dispatcher = SemaphoreDispatcher(
        semaphore_count=5,
        # monitor=CrawlerMonitor(
        #     # Maximum rows in live display
        #     max_visible_rows=20,          
        #     # DETAILED or AGGREGATED view
        #     display_mode=DisplayMode.DETAILED  
        # ),
        rate_limiter=RateLimiter(
            base_delay=(2.0, 4.0),          # Random delay between 2-4 seconds
            max_delay=30.0,                 # Cap delay at 30 seconds
            max_retries=3,                  # Retry up to 5 times on rate-limiting errors
            rate_limit_codes=[429, 503]     # Handle these HTTP status codes
        )
    )

    list_of_house_details = []
    urls = []
    for house in data:
        url = main_url + house['detail_url']
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
            logger.info(f"{GREEN}Successfully extracted house: {house_detail_data['address']}{RESET}")
            list_of_house_details.append(house_detail_data)
        else:
            logger.error(f"{RED}Error extracting property: {result.error_message}{RESET}")
    
    logger.info(f"{GREEN}Completed detailed property extraction. Successfully extracted {len(list_of_house_details)} out of {len(urls)} properties.{RESET}")
    return list_of_house_details
    