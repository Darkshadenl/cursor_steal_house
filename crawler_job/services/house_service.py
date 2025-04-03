from typing import AsyncGenerator, Dict, Any, List, Optional, Union, Tuple
import logging
from crawler_job.models.house_models import (
    DetailHouse,
    FetchedPage,
    GalleryHouse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from .repositories import (
    GalleryHouseRepository,
    DetailHouseRepository,
    FloorPlanRepository,
)
from .db_connection import get_db_session
from ..models.db_models import (
    DbGalleryHouse,
    DbDetailHouse,
    DbFloorPlan,
)
from ..helpers.transformers import (
    db_gallery_houses_to_pydantic,
    db_detail_houses_to_pydantic,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_repositories(
    session: Optional[AsyncSession] = None,
) -> AsyncGenerator[
    Dict[
        str, Union[GalleryHouseRepository, DetailHouseRepository, FloorPlanRepository]
    ],
    None,
]:
    """Context manager to get all repositories with a shared session"""
    session = session or get_db_session()
    try:
        yield {
            "gallery": GalleryHouseRepository(session),
            "detail": DetailHouseRepository(session),
            "floor_plan": FloorPlanRepository(session),
        }
    finally:
        await session.close()


class HouseService:
    """Service for handling house data storage"""

    def __init__(self, session: Optional[AsyncSession] = None):
        """Initialize with optional session"""
        self.session = session or get_db_session()

    async def store_gallery_houses(
        self, gallery_houses: List[GalleryHouse]
    ) -> Tuple[List[GalleryHouse], List[GalleryHouse]]:
        """
        Store a list of gallery houses and returns two lists of Pydantic models

        Returns:
            Tuple containing:
            - List of newly added GalleryHouse objects (Pydantic)
            - List of existing GalleryHouse objects (Pydantic)
        """
        logger.info(f"Storing {len(gallery_houses)} gallery houses to database...")

        new_db_houses: List[DbGalleryHouse] = []
        existing_db_houses: List[DbGalleryHouse] = []
        skipped_count = 0

        async with get_repositories(self.session) as repos:
            for house in gallery_houses:
                try:
                    # Check if the house already exists
                    existing_house: Optional[DbGalleryHouse] = await repos[
                        "gallery"
                    ].get_by_address(house.address, house.city)

                    if existing_house:
                        # House already exists, check if status changed
                        if existing_house.status != house.status:
                            existing_house.status = house.status
                            await repos["gallery"].update(existing_house)

                        # Add it to the existing houses list
                        existing_db_houses.append(existing_house)
                        skipped_count += 1
                        logger.info(
                            f"House already exists: {house.address}, {house.city}, using ID: {existing_house.id}"
                        )
                        continue

                    # Store in database
                    stored_db_house: DbGalleryHouse = await repos["gallery"].create(
                        house
                    )

                    # Add the stored house with its ID to our new houses list
                    new_db_houses.append(stored_db_house)

                    logger.info(
                        f"Stored gallery house: {stored_db_house.address}, {stored_db_house.city}"
                    )
                except Exception as e:
                    logger.error(f"Error storing gallery house: {str(e)}")

        if skipped_count > 0:
            logger.info(f"Skipped {skipped_count} existing houses")

        # Convert DB models to Pydantic models
        new_pydantic_houses = db_gallery_houses_to_pydantic(new_db_houses)
        existing_pydantic_houses = db_gallery_houses_to_pydantic(existing_db_houses)

        logger.info(
            f"Added {len(new_pydantic_houses)} new houses, found {len(existing_pydantic_houses)} existing houses"
        )

        return new_pydantic_houses, existing_pydantic_houses

    async def store_detail_houses(
        self, detail_houses: List[DetailHouse]
    ) -> List[DetailHouse]:
        """
        Store a list of detail houses and return Pydantic models

        Returns:
            - List of corresponding DetailHouse objects (Pydantic)
        """
        stored_db_houses: List[DbDetailHouse] = []

        for detail_house in detail_houses:
            db_detail_house = await self.store_detail_house(detail_house)
            if db_detail_house:
                stored_db_houses.append(db_detail_house)

        # Convert DB models to Pydantic models using the transformer function
        pydantic_houses = db_detail_houses_to_pydantic(stored_db_houses)

        return pydantic_houses

    async def store_detail_house(
        self, detail_house: DetailHouse
    ) -> Optional[DbDetailHouse]:
        """Store a detail house and return the detail house object"""
        async with get_repositories(self.session) as repos:
            try:
                # Check if house already exists
                existing_house: Optional[DbDetailHouse] = await repos[
                    "detail"
                ].get_by_address(
                    detail_house.address, detail_house.postal_code, detail_house.city
                )

                if existing_house:
                    # Compare fields to check for differences
                    db_detail_house = detail_house.to_db_model()
                    if existing_house.has_changes(db_detail_house):
                        detail_house_obj = await repos["detail"].update(
                            existing_house.id, detail_house
                        )
                        logger.info(
                            f"Updated detail house with changes: {detail_house_obj.address}, {detail_house_obj.city}"
                        )
                    else:
                        logger.info(
                            f"No changes needed for detail house: {existing_house.address}, {existing_house.city}"
                        )
                        detail_house_obj = existing_house
                else:
                    # Store new house in database
                    detail_house_obj = await repos["detail"].create(detail_house)
                    logger.info(
                        f"Stored new detail house: {detail_house_obj.address}, {detail_house_obj.city}"
                    )

                return detail_house_obj

            except Exception as e:
                logger.error(f"Error storing detail house: {str(e)}")
                return None

    async def store_crawler_results(
        self,
        gallery_data: List[GalleryHouse],
        detail_data: Optional[DetailHouse] = None,
    ) -> Dict[str, Any]:
        """Store crawler results including gallery and detail data"""
        result = {
            "new_houses": [],
            "existing_houses": [],
            "detail_id": None,
            "success": False,
        }

        try:
            # Store gallery houses
            if gallery_data:
                new_houses, existing_houses = await self.store_gallery_houses(
                    gallery_data
                )
                result["new_houses"] = new_houses
                result["existing_houses"] = existing_houses
                logger.info(
                    f"Stored {len(new_houses)} new houses, {len(existing_houses)} existing houses"
                )

            # Store detail house if available
            if detail_data:
                # If we have gallery data, try to find matching gallery house
                if result["new_houses"]:
                    matching_house = next(
                        (
                            house
                            for house in result["new_houses"]
                            if house.address == detail_data.address
                            and house.city == detail_data.city
                        ),
                        None,
                    )
                    if matching_house:
                        detail_data.gallery_id = getattr(
                            matching_house, "gallery_id", None
                        )

                detail_house = await self.store_detail_house(detail_data)
                if detail_house:
                    result["detail_id"] = detail_house.id
                    logger.info(f"Stored detail house with ID: {detail_house.id}")

            result["success"] = True
        except Exception as e:
            logger.error(f"Error in store_crawler_results: {str(e)}")
            result["error"] = str(e)

        logger.info(f"Crawler results stored successfully")
        return result
