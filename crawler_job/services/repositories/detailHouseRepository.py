from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List, Optional
import logging

from ...models.db_models import (
    DbDetailHouse,
)
from ...models.house_models import (
    DetailHouse,
)

logger = logging.getLogger(__name__)


class DetailHouseRepository:
    """Repository for DetailHouse operations"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, detail_id: int) -> Optional[DbDetailHouse]:
        """Get a detail house by ID"""
        result = await self.session.execute(
            select(DbDetailHouse).where(DbDetailHouse.id == detail_id)
        )
        return result.scalar_one_or_none()

    async def get_by_address(
        self, address: str, postal_code: str, city: str
    ) -> Optional[DbDetailHouse]:
        """Get a detail house by address, postal code, and city"""
        result = await self.session.execute(
            select(DbDetailHouse).where(
                DbDetailHouse.address == address,
                DbDetailHouse.postal_code == postal_code,
                DbDetailHouse.city == city,
            )
        )
        return result.scalar_one_or_none()

    async def get_by_gallery_id(self, gallery_id: int) -> Optional[DbDetailHouse]:
        """Get a detail house by gallery ID"""
        result = await self.session.execute(
            select(DbDetailHouse).where(DbDetailHouse.gallery_id == gallery_id)
        )
        return result.scalar_one_or_none()

    async def create(self, detail_house: DetailHouse) -> DbDetailHouse:
        """Create a new detail house"""
        db_house = detail_house.to_db_model()
        self.session.add(db_house)
        await self.session.flush()  # Get ID without committing

        # Add floor plans if they exist
        # if detail_house.floor_plans:
        #     for plan in detail_house.floor_plans:
        #         db_plan = plan.to_db_model(db_house.id)
        #         self.session.add(db_plan)

        await self.session.commit()
        logger.info(f"Created detail house: {db_house.address}, {db_house.city}")
        return db_house

    async def update(
        self, detail_id: int, detail_house: DetailHouse
    ) -> Optional[DbDetailHouse]:
        """Update an existing detail house"""
        db_house = await self.session.execute(
            select(DbDetailHouse).where(DbDetailHouse.id == detail_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return None

        # Update basic fields using the to_db_model method
        updated_db = detail_house.to_db_model()
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_"):
                setattr(db_house, key, value)

        await self.session.commit()
        logger.info(f"Updated detail house: {db_house.address}, {db_house.city}")
        return db_house

    async def get_or_create(self, detail_house: DetailHouse) -> DbDetailHouse:
        """Get an existing detail house or create a new one"""
        if not all([detail_house.address, detail_house.postal_code, detail_house.city]):
            raise ValueError(
                "Address, postal code, and city are required for detail house"
            )

        existing = None

        # Try to find by gallery_id if provided
        if detail_house.gallery_id:
            existing = await self.get_by_gallery_id(detail_house.gallery_id)

        # If not found, try to find by address
        if not existing:
            existing = await self.get_by_address(
                detail_house.address, detail_house.postal_code, detail_house.city
            )

        if existing:
            if existing.has_changes(detail_house.to_db_model()):
                return await self.update(existing.id, detail_house)
            return existing

        return await self.create(detail_house)

    async def delete(self, detail_id: int) -> bool:
        """Delete a detail house"""
        db_house = await self.session.execute(
            select(DbDetailHouse).where(DbDetailHouse.id == detail_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return False

        # Floor plans will be automatically deleted due to cascade
        await self.session.delete(db_house)
        await self.session.commit()
        logger.info(f"Deleted detail house with ID: {detail_id}")
        return True
