from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List, Optional
import logging

from ..models.db_models import (
    DbGalleryHouse,
    DbDetailHouse,
    DbFloorPlan,
)
from crawler_job.models.house_models import (
    GalleryHouse,
    DetailHouse,
    FloorPlan,
)
from .db_connection import get_db_session

logger = logging.getLogger(__name__)


class GalleryHouseRepository:
    """Repository for GalleryHouse operations"""

    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()

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

        # Convert to Pydantic and back to ensure proper transformation
        gallery_house = GalleryHouse.from_db_model(db_gallery_house)

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


class DetailHouseRepository:
    """Repository for DetailHouse operations"""

    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()

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
        if detail_house.floor_plans:
            for plan in detail_house.floor_plans:
                db_plan = plan.to_db_model(db_house.id)
                self.session.add(db_plan)

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


class FloorPlanRepository:
    """Repository for FloorPlan operations"""

    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()

    async def get_by_id(self, plan_id: int) -> Optional[DbFloorPlan]:
        """Get a floor plan by ID"""
        result = await self.session.execute(
            select(DbFloorPlan).where(DbFloorPlan.id == plan_id)
        )
        return result.scalar_one_or_none()

    async def get_by_house_id(self, house_id: int) -> List[DbFloorPlan]:
        """Get all floor plans for a house"""
        result = await self.session.execute(
            select(DbFloorPlan).where(DbFloorPlan.house_id == house_id)
        )
        return result.scalars().all()

    async def create(self, plan: FloorPlan, house_id: int) -> DbFloorPlan:
        """Create a new floor plan"""
        db_plan = plan.to_db_model(house_id)
        self.session.add(db_plan)
        await self.session.commit()
        logger.info(f"Created floor plan for house ID: {house_id}")
        return db_plan

    async def update(self, plan_id: int, plan: FloorPlan) -> Optional[DbFloorPlan]:
        """Update an existing floor plan"""
        db_plan = await self.session.execute(
            select(DbFloorPlan).where(DbFloorPlan.id == plan_id)
        )
        db_plan = db_plan.scalar_one_or_none()
        if not db_plan:
            return None

        # Create a new DB model from the Pydantic model
        updated_plan = plan.to_db_model(db_plan.house_id)

        # Update fields
        for key, value in updated_plan.__dict__.items():
            if not key.startswith("_") and key != "id" and key != "house_id":
                setattr(db_plan, key, value)

        await self.session.commit()
        logger.info(f"Updated floor plan with ID: {plan_id}")
        return db_plan

    async def delete(self, plan_id: int) -> bool:
        """Delete a floor plan"""
        db_plan = await self.session.execute(
            select(DbFloorPlan).where(DbFloorPlan.id == plan_id)
        )
        db_plan = db_plan.scalar_one_or_none()
        if not db_plan:
            return False

        await self.session.delete(db_plan)
        await self.session.commit()
        logger.info(f"Deleted floor plan with ID: {plan_id}")
        return True
