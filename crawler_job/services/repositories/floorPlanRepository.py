from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
import logging

from ...models.db_models import (
    DbFloorPlan,
)
from crawler_job.models.house_models import (
    FloorPlan,
)

logger = logging.getLogger(__name__)


class FloorPlanRepository:
    """Repository for FloorPlan operations"""

    def __init__(self, session: AsyncSession):
        self.session = session

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
