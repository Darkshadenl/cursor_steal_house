from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
import logging

from ...models.db_models import (
    DbGalleryHouse,
)
from ...models.house_models import (
    GalleryHouse,
)

logger = logging.getLogger(__name__)


class GalleryHouseRepository:
    """Repository for GalleryHouse operations"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, gallery_id: int) -> Optional[DbGalleryHouse]:
        """Get a gallery house by ID"""
        result = await self.session.execute(
            select(DbGalleryHouse).where(DbGalleryHouse.id == gallery_id)
        )
        return result.scalar_one_or_none()

    async def get_by_address(self, address: str, city: str) -> Optional[DbGalleryHouse]:
        """Get a gallery house by address and city"""
        result = await self.session.execute(
            select(DbGalleryHouse).where(
                DbGalleryHouse.address == address, DbGalleryHouse.city == city
            )
        )
        return result.scalar_one_or_none()

    async def create(self, gallery_house: GalleryHouse) -> DbGalleryHouse:
        """Create a new gallery house"""
        db_house = gallery_house.to_db_model()
        self.session.add(db_house)
        await self.session.commit()
        logger.info(f"Created gallery house: {db_house.address}, {db_house.city}")
        return db_house

    async def update(
        self, db_gallery_house: DbGalleryHouse
    ) -> Optional[DbGalleryHouse]:
        """Update an existing gallery house"""
        db_house = await self.session.execute(
            select(DbGalleryHouse).where(DbGalleryHouse.id == db_gallery_house.id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return None

        gallery_house = await GalleryHouse.from_db_model_async(db_gallery_house)

        # Apply updates from the pydantic model
        updated_db = gallery_house.to_db_model()
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_"):
                setattr(db_house, key, value)

        await self.session.commit()
        logger.info(f"Updated gallery house: {db_house.address}, {db_house.city}")
        return db_house

    async def get_or_create(self, gallery_house: GalleryHouse) -> DbGalleryHouse:
        """Get an existing gallery house or create a new one"""
        if not gallery_house.address or not gallery_house.city:
            raise ValueError("Address and city are required for gallery house")

        existing = await self.get_by_address(gallery_house.address, gallery_house.city)
        if existing:
            return existing

        return await self.create(gallery_house)

    async def delete(self, gallery_id: int) -> bool:
        """Delete a gallery house"""
        db_house = await self.session.execute(
            select(DbGalleryHouse).where(DbGalleryHouse.id == gallery_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return False

        await self.session.delete(db_house)
        await self.session.commit()
        logger.info(f"Deleted gallery house with ID: {gallery_id}")
        return True
