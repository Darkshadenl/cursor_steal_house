import json
import logging
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, DefaultMarkdownGenerator, JsonCssExtractionStrategy, LLMConfig, PruningContentFilter
from crawl4ai.extraction_strategy import LLMExtractionStrategy

# Import our models
from ..vesteda_models import (
    GalleryHouse
)

# Configure logging
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

async def execute_property_extraction(crawler: AsyncWebCrawler, url: str, session_id: str, deepseek_api_key: str):
    
    correct_urls = ['https://hurenbij.vesteda.com/zoekopdracht/', 'https://hurenbij.vesteda.com/zoekopdracht/#tab-content-inloggen']
    
    if (url not in correct_urls):
        logger.error(f"{RED}Invalid URL: {url}{RESET}")
        raise Exception("Invalid URL")
    
    logger.info(f"Starting property extraction from {url}")
    
    schema = {
        "name": "Houses",
        "baseSelector": "div.card.card-result-list",  # Basisselector voor elk huis
        "fields": [
            {"name": "address", "selector": "h5.card-title a", "type": "text"},  # Adres
            {"name": "city", "selector": "div.card-text", "type": "text"},  # Plaats
            {"name": "price", "selector": "div.object-price span.value", "type": "text"},  # Prijs
            {"name": "bedrooms", "selector": "div.object-rooms span.value", "type": "text"},  # Slaapkamers
            {"name": "area", "selector": "div.object-area span.value", "type": "text"},  # Woonoppervlakte
            {"name": "availability", "selector": "div.card-body.pt-0 a", "type": "text"},  # Beschikbaarheid
            {"name": "status", "selector": "div.card-image-label span", "type": "text"},  # Status (bijv. "For rent")
            {"name": "image", "selector": "img.card-img-top", "type": "attribute", "attribute": "src"}  # Afbeelding
        ]
    }
    
    # Step 1: Crawl the gallery page to extract house listings
    gallery_config = CrawlerRunConfig(
        # markdown_generator=markdown_generator,
        extraction_strategy=JsonCssExtractionStrategy(schema),
        cache_mode=CacheMode.BYPASS
    )
    
    # Execute the gallery page crawl
    result = await crawler.arun(url=url, config=gallery_config)
    
    if result.success:
        # 5. The extracted content is presumably JSON
        data = json.loads(result.extracted_content)
        logger.info(f"{GREEN}Successfully extracted {len(data)} properties{RESET}")        
        return data
    else:
        logger.error(f"{RED}Error extracting properties: {result.error_message}{RESET}")
        raise Exception("Error extracting properties", result.error_message)
    