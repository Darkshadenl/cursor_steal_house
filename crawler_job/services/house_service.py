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

    async def identify_new_houses(
        self, gallery_houses: List[GalleryHouse]
    ) -> List[GalleryHouse]:
        """Identificeer nieuwe huizen zonder database write"""
        new_houses = []
        async with get_repositories(self.session) as repos:
            for house in gallery_houses:
                existing_house = await repos["gallery"].get_by_address(
                    house.address, house.city
                )
                if not existing_house:
                    new_houses.append(house)
        return new_houses

    async def store_houses_atomic(
        self,
        gallery_houses: List[GalleryHouse],
        detail_houses: List[DetailHouse],
        all_houses: List[GalleryHouse],
    ) -> Dict[str, int]:
        """Atomic transaction voor alle huisdata"""
        async with self.session.begin():
            # Persisteer gallery houses
            new_houses, existing_houses = await self._store_gallery_houses(
                gallery_houses
            )

            # Match en persisteer detail houses
            matched_details = await self._match_details_with_gallery(
                detail_houses, all_houses
            )
            await self._store_detail_houses(matched_details)

            return {
                "new_count": len(new_houses),
                "existing_count": len(existing_houses),
            }

    async def _store_gallery_houses(
        self, gallery_houses: List[GalleryHouse]
    ) -> Tuple[List[GalleryHouse], List[GalleryHouse]]:
        """Interne methode voor gallery house opslag"""
        new_db_houses: List[DbGalleryHouse] = []
        existing_db_houses: List[DbGalleryHouse] = []

        async with get_repositories(self.session) as repos:
            for house in gallery_houses:
                existing_house = await repos["gallery"].get_by_address(
                    house.address, house.city
                )
                if existing_house:
                    if existing_house.status != house.status:
                        existing_house.status = house.status
                        await repos["gallery"].update(existing_house)
                    existing_db_houses.append(existing_house)
                else:
                    stored_db_house = await repos["gallery"].create(house)
                    new_db_houses.append(stored_db_house)

        return (
            db_gallery_houses_to_pydantic(new_db_houses),
            db_gallery_houses_to_pydantic(existing_db_houses),
        )

    async def _match_details_with_gallery(
        self, detail_houses: List[DetailHouse], all_houses: List[GalleryHouse]
    ) -> List[DetailHouse]:
        """Match detail houses met gallery houses"""
        matched_details = []
        for detail_house in detail_houses:
            matching_gallery = next(
                (
                    h
                    for h in all_houses
                    if h.address == detail_house.address and h.city == detail_house.city
                ),
                None,
            )
            if matching_gallery:
                detail_house.gallery_id = getattr(matching_gallery, "gallery_id", None)
                matched_details.append(detail_house)
        return matched_details

    async def _store_detail_houses(
        self, detail_houses: List[DetailHouse]
    ) -> List[DetailHouse]:
        """Interne methode voor detail house opslag"""
        stored_db_houses: List[DbDetailHouse] = []
        async with get_repositories(self.session) as repos:
            for detail_house in detail_houses:
                existing_house = await repos["detail"].get_by_address(
                    detail_house.address, detail_house.postal_code, detail_house.city
                )
                if existing_house:
                    db_detail_house = detail_house.to_db_model()
                    if existing_house.has_changes(db_detail_house):
                        await repos["detail"].update(existing_house.id, detail_house)
                else:
                    detail_house_obj = await repos["detail"].create(detail_house)
                    stored_db_houses.append(detail_house_obj)
        return db_detail_houses_to_pydantic(stored_db_houses)
