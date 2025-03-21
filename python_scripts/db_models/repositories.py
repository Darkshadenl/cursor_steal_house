from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional, Dict, Any
import logging

from .models import GalleryHouse, DetailHouse, FloorPlan
from .db_connection import get_db_session

logger = logging.getLogger(__name__)

class GalleryHouseRepository:
    """Repository for GalleryHouse operations"""
    
    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()
    
    async def get_by_id(self, gallery_id: int) -> Optional[GalleryHouse]:
        """Get a gallery house by ID"""
        result = await self.session.execute(
            select(GalleryHouse).where(GalleryHouse.id == gallery_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_address(self, address: str, city: str) -> Optional[GalleryHouse]:
        """Get a gallery house by address and city"""
        result = await self.session.execute(
            select(GalleryHouse).where(
                GalleryHouse.address == address,
                GalleryHouse.city == city
            )
        )
        return result.scalar_one_or_none()
    
    async def create(self, gallery_data: Dict[str, Any]) -> GalleryHouse:
        """Create a new gallery house"""
        gallery_house = GalleryHouse(**gallery_data)
        self.session.add(gallery_house)
        await self.session.commit()
        logger.info(f"Created gallery house: {gallery_house.address}, {gallery_house.city}")
        return gallery_house
    
    async def update(self, gallery_id: int, gallery_data: Dict[str, Any]) -> Optional[GalleryHouse]:
        """Update an existing gallery house"""
        gallery_house = await self.get_by_id(gallery_id)
        if not gallery_house:
            return None
        
        for key, value in gallery_data.items():
            if hasattr(gallery_house, key):
                setattr(gallery_house, key, value)
        
        await self.session.commit()
        logger.info(f"Updated gallery house: {gallery_house.address}, {gallery_house.city}")
        return gallery_house
    
    async def get_or_create(self, gallery_data: Dict[str, Any]) -> GalleryHouse:
        """Get an existing gallery house or create a new one"""
        address = gallery_data.get('address')
        city = gallery_data.get('city')
        
        if not address or not city:
            raise ValueError("Address and city are required for gallery house")
        
        existing = await self.get_by_address(address, city)
        if existing:
            # Update with new data
            for key, value in gallery_data.items():
                if hasattr(existing, key):
                    setattr(existing, key, value)
            await self.session.commit()
            logger.info(f"Updated existing gallery house: {existing.address}, {existing.city}")
            return existing
        
        # Create new
        return await self.create(gallery_data)
    
    async def delete(self, gallery_id: int) -> bool:
        """Delete a gallery house"""
        gallery_house = await self.get_by_id(gallery_id)
        if not gallery_house:
            return False
        
        await self.session.delete(gallery_house)
        await self.session.commit()
        logger.info(f"Deleted gallery house with ID: {gallery_id}")
        return True


class DetailHouseRepository:
    """Repository for DetailHouse operations"""
    
    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()
    
    async def get_by_id(self, detail_id: int) -> Optional[DetailHouse]:
        """Get a detail house by ID"""
        result = await self.session.execute(
            select(DetailHouse).where(DetailHouse.id == detail_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_address(self, address: str, postal_code: str, city: str) -> Optional[DetailHouse]:
        """Get a detail house by address, postal code, and city"""
        result = await self.session.execute(
            select(DetailHouse).where(
                DetailHouse.address == address,
                DetailHouse.postal_code == postal_code,
                DetailHouse.city == city
            )
        )
        return result.scalar_one_or_none()
    
    async def get_by_gallery_id(self, gallery_id: int) -> Optional[DetailHouse]:
        """Get a detail house by gallery ID"""
        result = await self.session.execute(
            select(DetailHouse).where(DetailHouse.gallery_id == gallery_id)
        )
        return result.scalar_one_or_none()
    
    async def create(self, detail_data: Dict[str, Any], gallery_id: Optional[int] = None) -> DetailHouse:
        """Create a new detail house"""
        if gallery_id:
            detail_data['gallery_id'] = gallery_id
            
        # Extract floor plans if they exist
        floor_plans_data = detail_data.pop('floor_plans', None)
        
        detail_house = DetailHouse(**detail_data)
        self.session.add(detail_house)
        await self.session.flush()  # Get ID without committing
        
        # Add floor plans if they exist
        if floor_plans_data and isinstance(floor_plans_data, list):
            for plan_data in floor_plans_data:
                plan = FloorPlan(house_id=detail_house.id, **plan_data)
                self.session.add(plan)
        
        await self.session.commit()
        logger.info(f"Created detail house: {detail_house.address}, {detail_house.city}")
        return detail_house
    
    async def update(self, detail_id: int, detail_data: Dict[str, Any]) -> Optional[DetailHouse]:
        """Update an existing detail house"""
        detail_house = await self.get_by_id(detail_id)
        if not detail_house:
            return None
        
        # Extract floor plans if they exist
        floor_plans_data = detail_data.pop('floor_plans', None)
        
        # Update detail house attributes
        for key, value in detail_data.items():
            if hasattr(detail_house, key):
                setattr(detail_house, key, value)
        
        # Handle floor plans update
        if floor_plans_data and isinstance(floor_plans_data, list):
            # Remove existing floor plans
            await self.session.execute(
                select(FloorPlan).where(FloorPlan.house_id == detail_id)
            ).delete()
            
            # Add new floor plans
            for plan_data in floor_plans_data:
                plan = FloorPlan(house_id=detail_id, **plan_data)
                self.session.add(plan)
        
        await self.session.commit()
        logger.info(f"Updated detail house: {detail_house.address}, {detail_house.city}")
        return detail_house
    
    async def get_or_create(self, detail_data: Dict[str, Any], gallery_id: Optional[int] = None) -> DetailHouse:
        """Get an existing detail house or create a new one"""
        address = detail_data.get('address')
        postal_code = detail_data.get('postal_code')
        city = detail_data.get('city')
        
        if not all([address, postal_code, city]):
            raise ValueError("Address, postal code, and city are required for detail house")
        
        existing = None
        
        # Try to find by gallery_id if provided
        if gallery_id:
            existing = await self.get_by_gallery_id(gallery_id)
        
        # If not found, try to find by address
        if not existing:
            existing = await self.get_by_address(address, postal_code, city)
        
        if existing:
            # Update with new data
            return await self.update(existing.id, detail_data)
        
        # Create new
        return await self.create(detail_data, gallery_id)
    
    async def delete(self, detail_id: int) -> bool:
        """Delete a detail house"""
        detail_house = await self.get_by_id(detail_id)
        if not detail_house:
            return False
        
        # Floor plans will be automatically deleted due to cascade
        await self.session.delete(detail_house)
        await self.session.commit()
        logger.info(f"Deleted detail house with ID: {detail_id}")
        return True


class FloorPlanRepository:
    """Repository for FloorPlan operations"""
    
    def __init__(self, session: Optional[AsyncSession] = None):
        self.session = session or get_db_session()
    
    async def get_by_id(self, plan_id: int) -> Optional[FloorPlan]:
        """Get a floor plan by ID"""
        result = await self.session.execute(
            select(FloorPlan).where(FloorPlan.id == plan_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_house_id(self, house_id: int) -> List[FloorPlan]:
        """Get all floor plans for a house"""
        result = await self.session.execute(
            select(FloorPlan).where(FloorPlan.house_id == house_id)
        )
        return result.scalars().all()
    
    async def create(self, plan_data: Dict[str, Any]) -> FloorPlan:
        """Create a new floor plan"""
        floor_plan = FloorPlan(**plan_data)
        self.session.add(floor_plan)
        await self.session.commit()
        logger.info(f"Created floor plan for house ID: {floor_plan.house_id}")
        return floor_plan
    
    async def update(self, plan_id: int, plan_data: Dict[str, Any]) -> Optional[FloorPlan]:
        """Update an existing floor plan"""
        floor_plan = await self.get_by_id(plan_id)
        if not floor_plan:
            return None
        
        for key, value in plan_data.items():
            if hasattr(floor_plan, key):
                setattr(floor_plan, key, value)
        
        await self.session.commit()
        logger.info(f"Updated floor plan with ID: {plan_id}")
        return floor_plan
    
    async def delete(self, plan_id: int) -> bool:
        """Delete a floor plan"""
        floor_plan = await self.get_by_id(plan_id)
        if not floor_plan:
            return False
        
        await self.session.delete(floor_plan)
        await self.session.commit()
        logger.info(f"Deleted floor plan with ID: {plan_id}")
        return True 