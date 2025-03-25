from typing import AsyncGenerator, Dict, Any, List, Optional, Union
import logging
from python_scripts.crawlers.vesteda.vesteda_models.house_models import (
    DetailHouse,
    FetchedPage,
    GalleryHouse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from ..db_models.repositories import (
    GalleryHouseRepository,
    DetailHouseRepository,
    FloorPlanRepository,
)
from ..db_models.db_connection import get_db_session
from ..db_models.models import (
    GalleryHouse as DBGalleryHouse,
    DetailHouse as DBDetailHouse,
    FloorPlan as DBFloorPlan,
)
from ..db_models.transformers import GalleryHouseTransformer, DetailHouseTransformer

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
    ) -> List[DBGalleryHouse]:
        """Store a list of gallery houses and return them with their IDs"""
        stored_houses = []
        skipped_count = 0

        async with get_repositories(self.session) as repos:
            for house in gallery_houses:
                try:
                    # Check if the house already exists
                    existing_house: Optional[DBGalleryHouse] = await repos[
                        "gallery"
                    ].get_by_address(house.address, house.city)

                    if existing_house:
                        # House already exists, check if status changed
                        if existing_house.status != house.status:
                            existing_house.status = house.status
                            await repos["gallery"].update(existing_house)

                        # Add it to the list
                        stored_houses.append(existing_house)
                        skipped_count += 1
                        logger.info(
                            f"House already exists: {house.address}, {house.city}, using ID: {existing_house.id}"
                        )
                        continue

                    # Store in database
                    stored_house: DBGalleryHouse = await repos["gallery"].create(house)

                    # Add the stored house with its ID to our list
                    stored_houses.append(stored_house)

                    logger.info(
                        f"Stored gallery house: {stored_house.address}, {stored_house.city}"
                    )
                except Exception as e:
                    logger.error(f"Error storing gallery house: {str(e)}")

        if skipped_count > 0:
            logger.info(f"Skipped {skipped_count} existing houses")

        return stored_houses

    async def store_detail_houses(
        self, detail_houses: List[DetailHouse]
    ) -> List[DBDetailHouse]:
        """Store a list of detail houses (inside FetchedPage.llm_output) and return their IDs"""
        stored_detailhouses: List[DBDetailHouse] = []
        for detail_house in detail_houses:
            dbDetailHouse: DBDetailHouse = await self.store_detail_house(detail_house)
            if dbDetailHouse:
                stored_detailhouses.append(dbDetailHouse)
        return stored_detailhouses

    async def store_detail_house(
        self, detail_house: DetailHouse
    ) -> Optional[DBDetailHouse]:
        """Store a detail house and return the detail house object"""
        async with get_repositories(self.session) as repos:
            try:
                # Check if house already exists
                existing_house: Optional[DBDetailHouse] = await repos[
                    "detail"
                ].get_by_address(
                    detail_house.address, detail_house.postal_code, detail_house.city
                )

                if existing_house:
                    # Compare fields to check for differences
                    if existing_house.has_changes(detail_house):
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
        result = {"gallery_houses": [], "detail_id": None, "success": False}

        try:
            # Store gallery houses
            if gallery_data:
                stored_houses = await self.store_gallery_houses(gallery_data)
                result["gallery_houses"] = stored_houses
                logger.info(f"Stored {len(stored_houses)} gallery houses")

            # Store detail house if available
            if detail_data:
                # If we have gallery data, link to the last gallery house
                gallery_id = (
                    result["gallery_houses"][-1].id
                    if result["gallery_houses"]
                    else None
                )

                detail_house = await self.store_detail_house(detail_data, gallery_id)
                if detail_house:
                    result["detail_id"] = detail_house.id
                    logger.info(f"Stored detail house with ID: {detail_house.id}")

            result["success"] = True
        except Exception as e:
            logger.error(f"Error in store_crawler_results: {str(e)}")
            result["error"] = str(e)

        logger.info(f"Crawler results stored successfully", result)
        return result
