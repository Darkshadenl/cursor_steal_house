from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
import logging

from ...models.db_models import (
    DbHouse,
)
from ...models.house_models import (
    House,
)

logger = logging.getLogger(__name__)


class HouseRepository:
    """Repository for House operations"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, house_id: int) -> Optional[DbHouse]:
        """Get a house by ID"""
        result = await self.session.execute(
            select(DbHouse).where(DbHouse.id == house_id)
        )
        return result.scalar_one_or_none()

    async def get_by_address(self, address: str, city: str) -> Optional[DbHouse]:
        """Get a house by address and city"""
        result = await self.session.execute(
            select(DbHouse).where(DbHouse.address == address, DbHouse.city == city)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> List[DbHouse]:
        """Get all houses"""
        result = await self.session.execute(select(DbHouse))
        return result.scalars().all()

    async def create(self, house: House) -> DbHouse:
        """Create a new house"""
        db_house = house.to_db_model()
        self.session.add(db_house)
        await self.session.commit()
        logger.info(f"Created house: {db_house.address}, {db_house.city}")
        return db_house

    async def update(self, house_id: int, house: House) -> Optional[DbHouse]:
        """Update an existing house"""
        db_house = await self.session.execute(
            select(DbHouse).where(DbHouse.id == house_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return None

        # Update fields using the to_db_model method
        updated_db = house.to_db_model()
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_") and key != "id":
                setattr(db_house, key, value)

        await self.session.commit()
        logger.info(f"Updated house: {db_house.address}, {db_house.city}")
        return db_house

    async def get_or_create(self, house: House) -> DbHouse:
        """Get an existing house or create a new one"""
        if not all([house.address, house.city]):
            raise ValueError("Address and city are required for house")

        existing = await self.get_by_address(house.address, house.city)
        if existing:
            if existing.has_changes(house.to_db_model()):
                return await self.update(existing.id, house)
            return existing

        return await self.create(house)

    async def delete(self, house_id: int) -> bool:
        """Delete a house"""
        db_house = await self.session.execute(
            select(DbHouse).where(DbHouse.id == house_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return False

        await self.session.delete(db_house)
        await self.session.commit()
        logger.info(f"Deleted house with ID: {house_id}")
        return True
