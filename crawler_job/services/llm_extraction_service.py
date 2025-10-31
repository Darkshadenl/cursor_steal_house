import json
from typing import Dict, Any, List, Optional
from crawler_job.models.house_models import House, FetchedPage
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class LlmExtractionService:
    def __init__(self):
        self.llm_service = LLMService()

    async def execute_llm_extraction(
        self, fetched_pages: List[FetchedPage]
    ) -> List[House]:
        schema = House.model_json_schema()
        houses: List[House] = []

        logger.info("Extracting structured data using LLM...")

        for page in fetched_pages:
            if not page.success:
                continue

            if not page.markdown:
                logger.warning(f"No markdown for {page.url}")
                continue

            try:
                extracted_data: Optional[Dict[str, Any]] = (
                    await self.llm_service.extract(page.markdown, schema)
                )

                if extracted_data is None or len(extracted_data) == 0:
                    logger.warning(
                        f"No data extracted for {page.url}. extracted_data is None or empty"
                    )
                    continue

                json_data = json.loads(extracted_data)  # type: ignore

                if json_data is None:
                    logger.warning(
                        f"No data extracted for {page.url}. json_data is None"
                    )
                    logger.debug(
                        f"Page.markdown: {page.markdown}, Extracted data: {extracted_data}"
                    )
                    continue

                house = House.from_dict(json_data)
                house.detail_url = page.url
                houses.append(house)
                logger.info(f"Successfully extracted data for {page.url}")
            except Exception as e:
                logger.warning(f"Error extracting data for {page.url}: {str(e)}")
                continue

        return houses
