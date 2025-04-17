import json
import logging
from typing import Any, Dict, List, Optional
from crawler_job.models.house_models import (
    House,
    FetchedPage,
)
from crawler_job.services.llm_service import LLMService, LLMProvider

logger = logging.getLogger(__name__)


async def execute_llm_extraction(
    fetched_pages: List[FetchedPage], provider: LLMProvider
) -> List[House]:
    """
    Extract structured data from markdown using LLM

    Args:
        fetched_pages: List of fetched detail pages
        provider: LLM provider to use

    Returns:
        List[House]: List of House objects with extracted data
    """
    llm_service = LLMService()
    schema = House.model_json_schema()
    houses: List[House] = []

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
            # Create House directly from the dict
            house = House.from_dict(json_data)
            houses.append(house)
            logger.info(f"Successfully extracted data for {page.url}")
        except Exception as e:
            logger.warning(f"Error extracting data for {page.url}: {str(e)}")
            continue

    return houses
