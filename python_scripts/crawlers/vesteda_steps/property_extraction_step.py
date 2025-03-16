from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, DefaultMarkdownGenerator, PruningContentFilter
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from typing import List, Dict, Any
from .cookie_acceptor import accept_cookies

async def execute_property_extraction(crawler: AsyncWebCrawler, url: str, session_id: str):
    
    correct_urls = ['https://hurenbij.vesteda.com/zoekopdracht/', 'https://hurenbij.vesteda.com/zoekopdracht/#tab-content-inloggen']
    
    if (url not in correct_urls):
        raise Exception("Invalid URL")
    
    print(f"Extracting properties from {url}")
    
    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed")
    )
    
    run_config = CrawlerRunConfig(
        session_id=session_id,
        cache_mode=CacheMode.BYPASS,
        markdown_generator=md_generator
    )
    
    result = await crawler.arun(url=url, config=run_config)
    
    # print(result.markdown.fit_markdown)
    
    print(result.markdown.fit_markdown)
    pass
    