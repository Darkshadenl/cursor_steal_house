import json
import logging
from typing import List
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    CacheMode,
    JsonCssExtractionStrategy,
)

# Import our models and transformer
from ....models.house_models import GalleryHouse
from crawler_job.helpers.transformers import GalleryHouseTransformer

# Configure logging
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


async def execute_property_extraction(
    crawler: AsyncWebCrawler, url: str, session_id: str
) -> List[GalleryHouse]:

    correct_urls = [
        "https://hurenbij.vesteda.com/zoekopdracht/",
        "https://hurenbij.vesteda.com/zoekopdracht/#tab-content-inloggen",
    ]

    if url not in correct_urls:
        logger.error(f"{RED}Invalid URL: {url}{RESET}")
        raise Exception("Invalid URL")

    logger.info(f"Starting property extraction from {url}")

    schema = {
        "name": "Houses",
        "baseSelector": "div.card.card-result-list",
        "fields": [
            {"name": "address", "selector": "h5.card-title a", "type": "text"},
            {"name": "city", "selector": "div.card-text", "type": "text"},
            {
                "name": "price",
                "selector": "div.object-price span.value",
                "type": "text",
            },
            {
                "name": "bedrooms",
                "selector": "div.object-rooms span.value",
                "type": "text",
            },
            {"name": "area", "selector": "div.object-area span.value", "type": "text"},
            {"name": "status", "selector": "div.card-image-label span", "type": "text"},
            {
                "name": "image_url",
                "selector": "img.card-img-top",
                "type": "attribute",
                "attribute": "src",
            },
            {
                "name": "demand_message",
                "selector": "div.card-body.pt-0 p.text-muted",
                "type": "text",
            },
            {
                "name": "detail_url",
                "selector": "h5.card-title a",
                "type": "attribute",
                "attribute": "href",
            },
        ],
    }

    # Step 1: Crawl the gallery page to extract house listings
    gallery_config = CrawlerRunConfig(
        extraction_strategy=JsonCssExtractionStrategy(schema),
        cache_mode=CacheMode.BYPASS,
        session_id=session_id,
    )

    # Execute the gallery page crawl
    result = await crawler.arun(url=url, config=gallery_config)

    if result.success:
        raw_data = json.loads(result.extracted_content)
        transformed_data = [
            GalleryHouseTransformer.dict_to_pydantic(house) for house in raw_data
        ]
        logger.info(
            f"{GREEN}Successfully extracted and transformed {len(transformed_data)} properties{RESET}"
        )
        return transformed_data
    else:
        logger.error(f"{RED}Error extracting properties: {result.error_message}{RESET}")
        raise Exception("Error extracting properties", result.error_message)
