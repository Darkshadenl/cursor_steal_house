import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, DefaultMarkdownGenerator, LLMConfig, PruningContentFilter
from crawl4ai.extraction_strategy import LLMExtractionStrategy

# Import our models
from ..vesteda_models import (
    GalleryHouse
)

async def execute_property_extraction(crawler: AsyncWebCrawler, url: str, session_id: str, deepseek_api_key: str):
    
    correct_urls = ['https://hurenbij.vesteda.com/zoekopdracht/', 'https://hurenbij.vesteda.com/zoekopdracht/#tab-content-inloggen']
    
    if (url not in correct_urls):
        raise Exception("Invalid URL")
    
    print(f"Extracting properties from {url}")
    
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
            schema={"type": "array", "items": GalleryHouse.model_json_schema()},
            extraction_type="schema",
            input_format="fit_markdown",
            instruction="""
            A markdown text will be provided with information about houses.
            Extract all house data displayed in this markdown text.
            For each house, get the address, city, price, number of bedrooms,
            surface area, status (for rent/for sale), and any messages about popularity.
            Also extract the URLs of images and links to detail pages if available.
            Carefully extract the bedrooms and surface area as integers.
            """,
            extra_args={"temperature": 0.1}
        )
    
    # Step 1: Crawl the gallery page to extract house listings
    gallery_config = CrawlerRunConfig(
        markdown_generator=markdown_generator,
        extraction_strategy=llm_config,
        cache_mode=CacheMode.BYPASS
    )
    
    # Execute the gallery page crawl
    gallery_result = await crawler.arun(url=url, config=gallery_config)
    
    if gallery_result.success:
        # 5. The extracted content is presumably JSON
        data = json.loads(gallery_result.extracted_content)
        print("Extracted items:", data)

            # 6. Show usage stats
        llm_config.show_usage()  #prints token usage
        return data
    else:
        print("Error extracting properties", gallery_result.error_message)
        raise Exception("Error extracting properties", gallery_result.error_message)
    