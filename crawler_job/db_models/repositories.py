from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List, Optional
import logging

from .models import (
    GalleryHouse as DBGalleryHouse,
    DetailHouse as DBDetailHouse,
    FloorPlan as DBFloorPlan,
)
from crawler_job.crawlers.vesteda.models.house_models import (
    GalleryHouse,
    DetailHouse,
    FloorPlan,
)
from ..db_models.db_connection import get_db_session
from ..db_models.transformers import (
    GalleryHouseTransformer,
    DetailHouseTransformer,
    FloorPlanTransformer,
)

logger = logging.getLogger(__name__)


class GalleryHouseRepository:
    """Repository for GalleryHouse operations"""

    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()

    async def get_by_id(self, gallery_id: int) -> Optional[DBGalleryHouse]:
        """Get a gallery house by ID"""
        result = await self.session.execute(
            select(DBGalleryHouse).where(DBGalleryHouse.id == gallery_id)
        )
        return result.scalar_one_or_none()

    async def get_by_address(self, address: str, city: str) -> Optional[DBGalleryHouse]:
        """Get a gallery house by address and city"""
        result = await self.session.execute(
            select(DBGalleryHouse).where(
                DBGalleryHouse.address == address, DBGalleryHouse.city == city
            )
        )
        return result.scalar_one_or_none()

    async def create(self, gallery_house: GalleryHouse) -> DBGalleryHouse:
        """Create a new gallery house"""
        self.high_demand_update(gallery_house)
        db_house = GalleryHouseTransformer.pydantic_to_db(gallery_house)
        self.session.add(db_house)
        await self.session.commit()
        logger.info(f"Created gallery house: {db_house.address}, {db_house.city}")
        return db_house

    def high_demand_update(self, gallery_house: DBGalleryHouse):
        if (
            gallery_house.demand_message
            == "This house has many viewing requests. Increase you chance by selecting a different property."
        ):
            gallery_house.high_demand = True

    async def update(self, gallery_house: DBGalleryHouse) -> Optional[DBGalleryHouse]:
        """Update an existing gallery house"""
        db_house = await self.session.execute(
            select(DBGalleryHouse).where(DBGalleryHouse.id == gallery_house.id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return None

        self.high_demand_update(gallery_house)
        updated_db = GalleryHouseTransformer.pydantic_to_db(gallery_house)
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_"):
                setattr(db_house, key, value)

        await self.session.commit()
        logger.info(f"Updated gallery house: {db_house.address}, {db_house.city}")
        return db_house

    async def get_or_create(self, gallery_house: GalleryHouse) -> DBGalleryHouse:
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
            select(DBGalleryHouse).where(DBGalleryHouse.id == gallery_id)
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

    async def get_by_id(self, detail_id: int) -> Optional[DBDetailHouse]:
        """Get a detail house by ID"""
        result = await self.session.execute(
            select(DBDetailHouse).where(DBDetailHouse.id == detail_id)
        )
        return result.scalar_one_or_none()

    async def get_by_address(
        self, address: str, postal_code: str, city: str
    ) -> Optional[DBDetailHouse]:
        """Get a detail house by address, postal code, and city"""
        result = await self.session.execute(
            select(DBDetailHouse).where(
                DBDetailHouse.address == address,
                DBDetailHouse.postal_code == postal_code,
                DBDetailHouse.city == city,
            )
        )
        return result.scalar_one_or_none()

    async def get_by_gallery_id(self, gallery_id: int) -> Optional[DBDetailHouse]:
        """Get a detail house by gallery ID"""
        result = await self.session.execute(
            select(DBDetailHouse).where(DBDetailHouse.gallery_id == gallery_id)
        )
        return result.scalar_one_or_none()

    async def create(self, detail_house: DetailHouse) -> DBDetailHouse:
        """Create a new detail house"""
        db_house = DetailHouseTransformer.pydantic_to_db(detail_house)
        self.session.add(db_house)
        await self.session.flush()  # Get ID without committing

        # Add floor plans if they exist
        if detail_house.floor_plans:
            for plan in detail_house.floor_plans:
                db_plan = FloorPlanTransformer.pydantic_to_db(plan, db_house.id)
                self.session.add(db_plan)

        await self.session.commit()
        logger.info(f"Created detail house: {db_house.address}, {db_house.city}")
        return db_house

    async def update(
        self, detail_id: int, detail_house: DetailHouse
    ) -> Optional[DBDetailHouse]:
        """Update an existing detail house"""
        db_house = await self.session.execute(
            select(DBDetailHouse).where(DBDetailHouse.id == detail_id)
        )
        db_house = db_house.scalar_one_or_none()
        if not db_house:
            return None

        # Update basic fields
        updated_db = DetailHouseTransformer.pydantic_to_db(detail_house)
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_"):
                setattr(db_house, key, value)

        await self.session.commit()
        logger.info(f"Updated detail house: {db_house.address}, {db_house.city}")
        return db_house

    async def get_or_create(self, detail_house: DetailHouse) -> DBDetailHouse:
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
            if existing.has_changes(detail_house):
                return await self.update(existing.id, detail_house)
            return existing

        return await self.create(detail_house)

    async def delete(self, detail_id: int) -> bool:
        """Delete a detail house"""
        db_house = await self.session.execute(
            select(DBDetailHouse).where(DBDetailHouse.id == detail_id)
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

    async def get_by_id(self, plan_id: int) -> Optional[DBFloorPlan]:
        """Get a floor plan by ID"""
        result = await self.session.execute(
            select(DBFloorPlan).where(DBFloorPlan.id == plan_id)
        )
        return result.scalar_one_or_none()

    async def get_by_house_id(self, house_id: int) -> List[DBFloorPlan]:
        """Get all floor plans for a house"""
        result = await self.session.execute(
            select(DBFloorPlan).where(DBFloorPlan.house_id == house_id)
        )
        return result.scalars().all()

    async def create(self, plan: FloorPlan, house_id: int) -> DBFloorPlan:
        """Create a new floor plan"""
        db_plan = FloorPlanTransformer.pydantic_to_db(plan, house_id)
        self.session.add(db_plan)
        await self.session.commit()
        logger.info(f"Created floor plan for house ID: {house_id}")
        return db_plan

    async def update(self, plan_id: int, plan: FloorPlan) -> Optional[DBFloorPlan]:
        """Update an existing floor plan"""
        db_plan = await self.session.execute(
            select(DBFloorPlan).where(DBFloorPlan.id == plan_id)
        )
        db_plan = db_plan.scalar_one_or_none()
        if not db_plan:
            return None

        updated_db = FloorPlanTransformer.pydantic_to_db(plan, db_plan.house_id)
        for key, value in updated_db.__dict__.items():
            if not key.startswith("_"):
                setattr(db_plan, key, value)

        await self.session.commit()
        logger.info(f"Updated floor plan with ID: {plan_id}")
        return db_plan

    async def delete(self, plan_id: int) -> bool:
        """Delete a floor plan"""
        db_plan = await self.session.execute(
            select(DBFloorPlan).where(DBFloorPlan.id == plan_id)
        )
        db_plan = db_plan.scalar_one_or_none()
        if not db_plan:
            return False

        await self.session.delete(db_plan)
        await self.session.commit()
        logger.info(f"Deleted floor plan with ID: {plan_id}")
        return True
