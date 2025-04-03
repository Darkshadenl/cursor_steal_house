from typing import List, Optional, Dict, Any
import logging

# Import Pydantic models
from crawler_job.models.house_models import (
    GalleryHouse,
    DetailHouse,
    FloorPlan,
)
from crawler_job.models.db_models import (
    DbGalleryHouse,
    DbDetailHouse,
    DbFloorPlan,
)

logger = logging.getLogger(__name__)


async def db_gallery_houses_to_pydantic_async(
    db_houses: List[DbGalleryHouse],
) -> List[GalleryHouse]:
    """Convert a list of DbGalleryHouse SQLAlchemy models to GalleryHouse Pydantic models"""
    return [await GalleryHouse.from_db_model_async(house) for house in db_houses]


async def db_detail_houses_to_pydantic_async(
    db_houses: List[DbDetailHouse],
) -> List[DetailHouse]:
    """Convert a list of DbDetailHouse SQLAlchemy models to DetailHouse Pydantic models"""
    return [await DetailHouse.from_db_model_async(house) for house in db_houses]


async def db_floor_plans_to_pydantic_async(
    db_plans: List[DbFloorPlan],
) -> List[FloorPlan]:
    """Convert a list of DbFloorPlan SQLAlchemy models to FloorPlan Pydantic models"""
    return [await FloorPlan.from_db_model_async(plan) for plan in db_plans]


def pydantic_gallery_houses_to_db(houses: List[GalleryHouse]) -> List[DbGalleryHouse]:
    """Convert a list of GalleryHouse Pydantic models to DbGalleryHouse SQLAlchemy models"""
    return [house.to_db_model() for house in houses]


def pydantic_detail_houses_to_db(houses: List[DetailHouse]) -> List[DbDetailHouse]:
    """Convert a list of DetailHouse Pydantic models to DbDetailHouse SQLAlchemy models"""
    return [house.to_db_model() for house in houses]


def pydantic_floor_plans_to_db(
    plans: List[FloorPlan], house_id: int
) -> List[DbFloorPlan]:
    """Convert a list of FloorPlan Pydantic models to DbFloorPlan SQLAlchemy models"""
    return [plan.to_db_model(house_id) for plan in plans]
