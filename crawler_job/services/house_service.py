from typing import AsyncGenerator, Dict, Any, List, Optional, Union, Tuple
import logging
from crawler_job.models.house_models import (
    DetailHouse,
    GalleryHouse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
import warnings

from .repositories import (
    GalleryHouseRepository,
    DetailHouseRepository,
    FloorPlanRepository,
)
from .db_connection import get_db_session
from ..models.db_models import (
    DbGalleryHouse,
    DbDetailHouse,
)
from ..helpers.transformers import (
    db_gallery_houses_to_pydantic_async,
    db_detail_houses_to_pydantic_async,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_repositories(
    session: AsyncSession,
) -> AsyncGenerator[
    Dict[
        str, Union[GalleryHouseRepository, DetailHouseRepository, FloorPlanRepository]
    ],
    None,
]:
    """Context manager to get all repositories with a shared session"""
    try:
        yield {
            "gallery": GalleryHouseRepository(session),
            "detail": DetailHouseRepository(session),
            "floor_plan": FloorPlanRepository(session),
        }
    finally:
        pass


class HouseService:
    """Service for handling house data storage"""

    def __init__(self):
        """Initialize with a new database session"""
        self.session = get_db_session()
        self._closed = False

    async def __aenter__(self):
        """Enter the context manager"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager and close the session"""
        await self.close()

    async def close(self):
        """Explicitly close the session"""
        if not self._closed:
            await self.session.close()
            self._closed = True

    def __del__(self):
        """Attempt to clean up resources when object is garbage collected"""
        if not self._closed:
            warnings.warn(
                "HouseService was not properly closed. "
                "Please use 'async with' statement or call 'await service.close()' explicitly.",
                ResourceWarning,
                stacklevel=2,
            )
            # We can't use await in __del__, so we just make a warning

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
        has_active_transaction = self.session.in_transaction()

        async def _execute_transaction():
            async with get_repositories(self.session) as repos:
                new_houses, existing_houses = (
                    await self._store_gallery_houses_with_repos(gallery_houses, repos)
                )

                matched_details = await self._match_details_with_gallery(
                    detail_houses, all_houses
                )
                await self._store_detail_houses_with_repos(matched_details, repos)

                return {
                    "new_count": len(new_houses),
                    "existing_count": len(existing_houses),
                }

        if has_active_transaction:
            return await _execute_transaction()
        else:
            async with self.session.begin():
                return await _execute_transaction()

    async def _store_gallery_houses_with_repos(
        self, gallery_houses: List[GalleryHouse], repos: Dict[str, Any]
    ) -> Tuple[List[GalleryHouse], List[GalleryHouse]]:
        """Interne methode voor gallery house opslag met gegeven repositories"""
        new_db_houses: List[DbGalleryHouse] = []
        existing_db_houses: List[DbGalleryHouse] = []

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
            await db_gallery_houses_to_pydantic_async(new_db_houses),
            await db_gallery_houses_to_pydantic_async(existing_db_houses),
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

    async def _store_detail_houses_with_repos(
        self, detail_houses: List[DetailHouse], repos: Dict[str, Any]
    ) -> List[DetailHouse]:
        """Interne methode voor detail house opslag met gegeven repositories"""
        stored_db_houses: List[DbDetailHouse] = []

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

        return await db_detail_houses_to_pydantic_async(stored_db_houses)

    async def _store_gallery_houses(
        self, gallery_houses: List[GalleryHouse]
    ) -> Tuple[List[GalleryHouse], List[GalleryHouse]]:
        """Interne methode voor gallery house opslag"""
        async with get_repositories(self.session) as repos:
            return await self._store_gallery_houses_with_repos(gallery_houses, repos)

    async def _store_detail_houses(
        self, detail_houses: List[DetailHouse]
    ) -> List[DetailHouse]:
        """Interne methode voor detail house opslag"""
        async with get_repositories(self.session) as repos:
            return await self._store_detail_houses_with_repos(detail_houses, repos)
