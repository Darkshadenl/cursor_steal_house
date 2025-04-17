import json
import logging
from typing import List
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    CacheMode,
    JsonCssExtractionStrategy,
)

from ....models.house_models import House

# Configure logging
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


async def execute_property_extraction(
    crawler: AsyncWebCrawler, url: str, session_id: str
) -> List[House]:
    """
    Extract property listings from the Vesteda search page and return them as House objects.

    Args:
        crawler: The web crawler instance
        url: The URL to crawl
        session_id: The session ID for the crawler

    Returns:
        List[House]: List of extracted House objects
    """
    logger.info("Extracting property listings...")

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

    # Crawl the gallery page to extract house listings
    gallery_config = CrawlerRunConfig(
        extraction_strategy=JsonCssExtractionStrategy(schema),
        cache_mode=CacheMode.BYPASS,
        session_id=session_id,
        magic=False,
        user_agent_mode="random",
    )

    # Execute the gallery page crawl
    result = await crawler.arun(url=url, config=gallery_config)

    if result.success:
        raw_data = json.loads(result.extracted_content)
        houses = []

        for house_data in raw_data:
            # Pre-process the data before passing to from_dict
            processed_data = house_data.copy()

            # Process bedrooms field
            try:
                if "bedrooms" in house_data and house_data["bedrooms"]:
                    processed_data["bedrooms"] = int(house_data["bedrooms"])
            except ValueError:
                logger.warning(
                    f"Could not convert bedrooms to int: {house_data.get('bedrooms')}"
                )
                processed_data["bedrooms"] = None

            # Process area field to square_meters
            try:
                if "area" in house_data and house_data["area"]:
                    # Strip "m²" and convert to int
                    area_str = house_data.get("area", "").replace("m2", "").strip()
                    if area_str:
                        processed_data["square_meters"] = int(area_str)
            except ValueError:
                logger.warning(
                    f"Could not convert area to int: {house_data.get('area')}"
                )
                processed_data["square_meters"] = None

            # Rename price to rental_price
            if "price" in processed_data:
                processed_data["rental_price"] = processed_data.pop("price")

            # Check if demand message indicates high demand
            demand_message = processed_data.get("demand_message")
            high_demand = False
            if demand_message and any(
                keyword in demand_message.lower()
                for keyword in ["hoge interesse", "veel interesse", "popular"]
            ):
                high_demand = True
            processed_data["high_demand"] = high_demand

            # Create House object using from_dict
            house = House.from_dict(processed_data)
            houses.append(house)

        logger.info(
            f"{GREEN}Successfully extracted and transformed {len(houses)} properties{RESET}"
        )
        return houses
    else:
        logger.error(f"{RED}Error extracting properties: {result.error_message}{RESET}")
        raise Exception("Error extracting properties", result.error_message)
