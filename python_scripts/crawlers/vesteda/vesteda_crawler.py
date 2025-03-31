import asyncio
import os
import logging
from crawl4ai import AsyncWebCrawler, BrowserConfig
from dotenv import load_dotenv

from python_scripts.crawlers.vesteda.vesteda_steps.detailed_property_extraction import (
    execute_detailed_property_extraction,
)
from .vesteda_steps.login_step import execute_login_step
from .vesteda_steps.search_navigation_step import execute_search_navigation
from .vesteda_steps.property_extraction_step import execute_property_extraction
from .vesteda_steps.cookie_acceptor import accept_cookies
from .vesteda_steps.llm_extraction_step import execute_llm_extraction
from python_scripts.services.house_service import HouseService
from python_scripts.crawlers.vesteda.models.house_models import (
    DetailHouse,
    FetchedPage,
    GalleryHouse,
)
from python_scripts.services.llm_service import LLMProvider
from python_scripts.db_models.models import (
    GalleryHouse as DBGalleryHouse,
    DetailHouse as DBDetailHouse,
)
from typing import List

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
            use_managed_browser=False,
            user_data_dir="./browser_data/vesteda",
            extra_args=[
                "--no-sandbox",
                "--disable-gpu",
            ],
        )
        self.base_url = "https://hurenbij.vesteda.com"
        self.email = os.getenv("VESTEDA_EMAIL")
        self.password = os.getenv("VESTEDA_PASSWORD")
        self.session_id = "vesteda_session"
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.house_service = HouseService()

    async def run_full_crawl(self):
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

                # Extract property listings
                logger.info("Extracting property listings...")
                gallery_data: List[GalleryHouse] = await execute_property_extraction(
                    crawler, url, self.session_id
                )

                # Store gallery data only
                logger.info(
                    f"Storing {len(gallery_data)} gallery houses to database..."
                )
                stored_houses: List[DBGalleryHouse] = (
                    await self.house_service.store_gallery_houses(gallery_data)
                )
                fetched_pages: List[FetchedPage] = (
                    await execute_detailed_property_extraction(
                        crawler, gallery_data, self.session_id
                    )
                )

                # Extract structured data using LLM
                logger.info("Extracting structured data using LLM...")
                detail_houses: List[DetailHouse] = await execute_llm_extraction(
                    fetched_pages, provider=LLMProvider.GEMINI
                )

                # Match detail houses with gallery houses based on address and city
                for detail_house in detail_houses:
                    matching_gallery_house = next(
                        (
                            house
                            for house in stored_houses
                            if house.address == detail_house.address
                            and house.city == detail_house.city
                        ),
                        None,
                    )

                    if matching_gallery_house:
                        detail_house.gallery_id = matching_gallery_house.id
                    else:
                        logger.warning(
                            f"No matching gallery house found for {detail_house.address}, {detail_house.city}"
                        )

                # Store detail houses
                logger.info(
                    f"Storing {len(detail_houses)} detail houses to database..."
                )
                stored_detail_houses: List[DBDetailHouse] = (
                    await self.house_service.store_detail_houses(detail_houses)
                )

                return {
                    "gallery_count": len(gallery_data),
                    "detail_count": len(stored_detail_houses),
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
