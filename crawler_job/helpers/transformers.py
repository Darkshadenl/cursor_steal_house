from typing import List, Optional, Dict, Any
import logging

# Import Pydantic models
from crawler_job.models.house_models import (
    House,
)
from crawler_job.models.db_models import (
    DbHouse,
)

logger = logging.getLogger(__name__)


async def db_houses_to_pydantic_async(
    db_houses: List[DbHouse],
) -> List[House]:
    """Convert a list of DbHouse SQLAlchemy models to House Pydantic models"""
    return [await House.from_db_model_async(house) for house in db_houses]


def pydantic_houses_to_db(houses: List[House]) -> List[DbHouse]:
    """Convert a list of House Pydantic models to DbHouse SQLAlchemy models"""
    return [house.to_db_model() for house in houses]
