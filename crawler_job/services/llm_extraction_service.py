import asyncio
import json
from typing import Dict, Any, List, Optional
from crawler_job.models.house_models import House, FetchedPage
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class LlmExtractionService:
    def __init__(self):
        self.llm_service = LLMService()

    async def _extract_single_page_async(
        self, page: FetchedPage, schema: Dict[str, Any]
    ) -> Optional[House]:
        if not page.success:
            return None

        if not page.markdown:
            logger.warning(f"No markdown for {page.url}")
            return None

        try:
            extracted_data: Optional[Dict[str, Any]] = await self.llm_service.extract(
                page.markdown, schema
            )

            if extracted_data is None or len(extracted_data) == 0:
                logger.warning(
                    f"No data extracted for {page.url} extracted_data is None or empty"
                )
                return None

            json_data = json.loads(extracted_data)  # type: ignore

            if json_data is None:
                logger.warning(f"No data extracted for {page.url} json_data is None")
                logger.debug(
                    f"Page.markdown: {page.markdown}, Extracted data: {extracted_data}"
                )
                return None

            house = House.from_dict(json_data)
            house.detail_url = page.url
            logger.info(f"Successfully extracted data for {page.url}")
            return house
        except Exception as e:
            logger.warning(f"Error extracting data for {page.url}: {str(e)}")
            return None

    async def execute_llm_extraction(
        self, fetched_pages: List[FetchedPage]
    ) -> List[House]:
        schema = House.model_json_schema()
        houses: List[House] = []

        logger.info("Extracting structured data using LLM...")

        chunk_size = 3
        for i in range(0, len(fetched_pages), chunk_size):
            chunk = fetched_pages[i : i + chunk_size]
            logger.info(
                f"Processing chunk {i // chunk_size + 1}/{(len(fetched_pages) + chunk_size - 1) // chunk_size}"
            )

            results = await asyncio.gather(
                *[self._extract_single_page_async(page, schema) for page in chunk]
            )

            houses.extend([house for house in results if house is not None])

        return houses
