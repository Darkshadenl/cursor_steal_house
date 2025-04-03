import asyncio
import os
import logging
from crawl4ai import AsyncWebCrawler, BrowserConfig
from dotenv import load_dotenv

from .vesteda_steps import (
    execute_detailed_property_extraction,
    execute_login_step,
    execute_search_navigation,
    execute_property_extraction,
    accept_cookies,
    execute_llm_extraction,
)
from crawler_job.services.house_service import HouseService
from crawler_job.models.house_models import (
    DetailHouse,
    FetchedPage,
    GalleryHouse,
)
from crawler_job.services.llm_service import LLMProvider
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("vesteda_crawler.log")],
)
logger = logging.getLogger(__name__)

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


class VestedaCrawler:
    def __init__(self):
        load_dotenv()
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=True,
            use_persistent_context=True,
            user_data_dir="./browser_data/vesteda",
        )
        self.base_url = "https://hurenbij.vesteda.com"
        self.email = os.getenv("VESTEDA_EMAIL")
        self.password = os.getenv("VESTEDA_PASSWORD")
        self.session_id = "vesteda_session"
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.house_service = HouseService()

    async def run_full_crawl(self) -> Dict[str, Any]:
        """Run a full crawl of Vesteda website and store results in database"""
        try:
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                # Navigate to search page
                url = await execute_search_navigation(crawler, self.session_id)

                # Handle login if needed
                if url == "https://hurenbij.vesteda.com/login/":
                    logger.info("Login required. Accepting cookies and logging in...")
                    await accept_cookies(crawler, url, self.session_id)
                    await execute_login_step(
                        crawler, self.email, self.password, self.session_id
                    )
                    url = await execute_search_navigation(crawler, self.session_id)

                # Extract property listing
                gallery_data: List[GalleryHouse] = await execute_property_extraction(
                    crawler, url, self.session_id
                )

                # Store gallery data - returns new and existing houses
                new_houses, existing_houses = (
                    await self.house_service.store_gallery_houses(gallery_data)
                )

                # Combine all houses for further processing
                all_houses = new_houses + existing_houses

                # Extract detailed property information - only for new houses to save resources
                if new_houses:
                    logger.info(f"Fetching details for {len(new_houses)} new houses...")
                    fetched_pages: List[FetchedPage] = (
                        await execute_detailed_property_extraction(
                            crawler, new_houses, self.session_id
                        )
                    )

                    # Extract structured data using LLM
                    detail_houses: List[DetailHouse] = await execute_llm_extraction(
                        fetched_pages, provider=LLMProvider.GEMINI
                    )

                    # Match detail houses with gallery houses based on address and city
                    for detail_house in detail_houses:
                        matching_gallery_house = next(
                            (
                                house
                                for house in all_houses
                                if house.address == detail_house.address
                                and house.city == detail_house.city
                            ),
                            None,
                        )

                        if matching_gallery_house:
                            # Use the gallery_id from the matching house if available
                            detail_house.gallery_id = getattr(
                                matching_gallery_house, "gallery_id", None
                            )
                        else:
                            logger.warning(
                                f"No matching gallery house found for {detail_house.address}, {detail_house.city}"
                            )

                    # Store detail houses
                    logger.info(
                        f"Storing {len(detail_houses)} detail houses to database..."
                    )
                    stored_detail_houses: List[DetailHouse] = (
                        await self.house_service.store_detail_houses(detail_houses)
                    )

                    return {
                        "gallery_count": len(gallery_data),
                        "new_houses_count": len(new_houses),
                        "existing_houses_count": len(existing_houses),
                        "detail_count": len(stored_detail_houses),
                        "success": True,
                    }
                else:
                    logger.info("No new houses found, skipping detail extraction")
                    return {
                        "gallery_count": len(gallery_data),
                        "new_houses_count": 0,
                        "existing_houses_count": len(existing_houses),
                        "detail_count": 0,
                        "success": True,
                    }

        except Exception as e:
            logger.error(f"{RED}Error during crawl: {str(e)}{RESET}")
            raise e


if __name__ == "__main__":
    crawler = VestedaCrawler()
    try:
        logger.info("Starting vesteda crawl...")
        result = asyncio.run(crawler.run_full_crawl())
        logger.info(f"{GREEN}Crawl completed successfully!{RESET}")
    except Exception as e:
        logger.error(f"{RED}Error during crawl: {str(e)}{RESET}")
        raise e
