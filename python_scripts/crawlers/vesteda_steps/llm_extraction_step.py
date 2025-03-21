import json
import logging
from typing import List
from python_scripts.crawlers.vesteda_models.house_models import FetchedPage, DetailHouse
from python_scripts.db_models.transformers import DetailHouseTransformer
from python_scripts.services.llm_service import LLMService, LLMProvider

logger = logging.getLogger(__name__)

async def execute_llm_extraction(fetched_pages: List[FetchedPage], provider: LLMProvider) -> List[FetchedPage]:
    """Extract structured data from markdown using LLM"""
    llm_service = LLMService()
    schema = DetailHouse.model_json_schema()
    
    for page in fetched_pages:
        if not page.success:
            continue
            
        try:
            extracted_data = await llm_service.extract(page.markdown, schema, provider)
                
            if extracted_data:
                json_data = json.loads(extracted_data)
                page.llm_output = DetailHouseTransformer.dict_to_pydantic(json_data)
                logger.info(f"Successfully extracted data for {page.url}")
            else:
                logger.warning(f"No data extracted for {page.url}")
                
        except Exception as e:
            logger.error(f"Error extracting data for {page.url}: {str(e)}")
            
    return fetched_pages