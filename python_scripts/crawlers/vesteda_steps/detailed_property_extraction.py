import json
from typing import List
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig, DefaultMarkdownGenerator, LLMConfig, LLMExtractionStrategy, PruningContentFilter

from python_scripts.crawlers.vesteda_models.house_models import DetailHouse, GalleryHouse

async def execute_detailed_property_extraction(crawler: AsyncWebCrawler, data: List[GalleryHouse], session_id: str, deepseek_api_key: str):
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
        # extraction_strategy=llm_config,
        cache_mode=CacheMode.BYPASS
    )
    
    list_of_house_details = []
    
    for house in data:
        url = house['detail_url']
        result = await crawler.arun(url=url, config=config)
    
        if result.success:
            house_detail_data = json.loads(result.extracted_content)
            llm_config.show_usage()  #prints token usage
            print(f"Extracted house: ")
            print(house_detail_data)
            list_of_house_details.append(house_detail_data)
        else:
            print("Error extracting properties", result.error_message)
            raise Exception("Error extracting properties", result.error_message)
    