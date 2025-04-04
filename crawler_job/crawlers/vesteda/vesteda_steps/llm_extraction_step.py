import json
import logging
from typing import Any, Dict, List, Optional
from crawler_job.models.house_models import (
    DetailHouse,
    FetchedPage,
)
from crawler_job.services.llm_service import LLMService, LLMProvider

logger = logging.getLogger(__name__)


async def execute_llm_extraction(
    fetched_pages: List[FetchedPage], provider: LLMProvider
) -> List[DetailHouse]:
    """Extract structured data from markdown using LLM"""
    llm_service = LLMService()
    schema = DetailHouse.model_json_schema()
    detail_houses: List[DetailHouse] = []

    logger.info("Extracting structured data using LLM...")

    for page in fetched_pages:
        if not page.success:
            continue

        try:
            extracted_data: Optional[Dict[str, Any] | None] = await llm_service.extract(
                page.markdown, schema, provider
            )

            if extracted_data is None:
                logger.warning(f"No data extracted for {page.url}")
                continue

            json_data = json.loads(extracted_data)
            # Create DetailHouse directly from the dict
            detail_house = DetailHouse.from_dict(json_data)
            detail_houses.append(detail_house)
            logger.info(f"Successfully extracted data for {page.url}")
        except Exception as e:
            logger.warning(f"No data extracted for {page.url}")
            continue

    return detail_houses
