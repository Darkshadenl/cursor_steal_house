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
    """Convert a list of DbHouse SQLAlchemy models to House Pydantic models

    Args:
        db_houses: List of DbHouse SQLAlchemy models to convert

    Returns:
        List[House]: Converted list of House Pydantic models
    """
    return [await House.from_db_model_async(house) for house in db_houses]


def db_houses_to_pydantic(
    db_houses: List[DbHouse],
) -> List[House]:
    """Synchronous version to convert a list of DbHouse SQLAlchemy models to House Pydantic models

    Note: This uses the non-async from_dict method, which may not have access to
    relationships that require async loading.

    Args:
        db_houses: List of DbHouse SQLAlchemy models to convert

    Returns:
        List[House]: Converted list of House Pydantic models
    """
    houses = []
    for db_house in db_houses:
        # Convert SQLAlchemy model to dict
        house_dict = {
            column.name: getattr(db_house, column.name)
            for column in db_house.__table__.columns
        }
        house = House.from_dict(house_dict)
        houses.append(house)
    return houses


def pydantic_houses_to_db(houses: List[House]) -> List[DbHouse]:
    """Convert a list of House Pydantic models to DbHouse SQLAlchemy models

    Args:
        houses: List of House Pydantic models to convert

    Returns:
        List[DbHouse]: Converted list of DbHouse SQLAlchemy models
    """
    return [house.to_db_model() for house in houses]
