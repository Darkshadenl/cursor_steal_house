from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
import logging

from .models import GalleryHouse, DetailHouse, FloorPlan
from .db_connection import get_db_session

logger = logging.getLogger(__name__)

class GalleryHouseRepository:
    """Repository for GalleryHouse operations"""
    
    def __init__(self, session: Optional[Session] = None):
        self.session = session or get_db_session()
    
    def get_by_id(self, gallery_id: int) -> Optional[GalleryHouse]:
        """Get a gallery house by ID"""
        return self.session.query(GalleryHouse).filter(GalleryHouse.id == gallery_id).first()
    
    def get_by_address(self, address: str, city: str) -> Optional[GalleryHouse]:
        """Get a gallery house by address and city"""
        return self.session.query(GalleryHouse).filter(
            GalleryHouse.address == address,
            GalleryHouse.city == city
        ).first()
    
    def create(self, gallery_data: Dict[str, Any]) -> GalleryHouse:
        """Create a new gallery house"""
        gallery_house = GalleryHouse(**gallery_data)
        self.session.add(gallery_house)
        self.session.commit()
        logger.info(f"Created gallery house: {gallery_house.address}, {gallery_house.city}")
        return gallery_house
    
    def update(self, gallery_id: int, gallery_data: Dict[str, Any]) -> Optional[GalleryHouse]:
        """Update an existing gallery house"""
        gallery_house = self.get_by_id(gallery_id)
        if not gallery_house:
            return None
        
        for key, value in gallery_data.items():
            if hasattr(gallery_house, key):
                setattr(gallery_house, key, value)
        
        self.session.commit()
        logger.info(f"Updated gallery house: {gallery_house.address}, {gallery_house.city}")
        return gallery_house
    
    def get_or_create(self, gallery_data: Dict[str, Any]) -> GalleryHouse:
        """Get an existing gallery house or create a new one"""
        address = gallery_data.get('address')
        city = gallery_data.get('city')
        
        if not address or not city:
            raise ValueError("Address and city are required for gallery house")
        
        existing = self.get_by_address(address, city)
        if existing:
            # Update with new data
            for key, value in gallery_data.items():
                if hasattr(existing, key):
                    setattr(existing, key, value)
            self.session.commit()
            logger.info(f"Updated existing gallery house: {existing.address}, {existing.city}")
            return existing
        
        # Create new
        return self.create(gallery_data)
    
    def delete(self, gallery_id: int) -> bool:
        """Delete a gallery house"""
        gallery_house = self.get_by_id(gallery_id)
        if not gallery_house:
            return False
        
        self.session.delete(gallery_house)
        self.session.commit()
        logger.info(f"Deleted gallery house with ID: {gallery_id}")
        return True


class DetailHouseRepository:
    """Repository for DetailHouse operations"""
    
    def __init__(self, session: Optional[Session] = None):
        self.session = session or get_db_session()
    
    def get_by_id(self, detail_id: int) -> Optional[DetailHouse]:
        """Get a detail house by ID"""
        return self.session.query(DetailHouse).filter(DetailHouse.id == detail_id).first()
    
    def get_by_address(self, address: str, postal_code: str, city: str) -> Optional[DetailHouse]:
        """Get a detail house by address, postal code, and city"""
        return self.session.query(DetailHouse).filter(
            DetailHouse.address == address,
            DetailHouse.postal_code == postal_code,
            DetailHouse.city == city
        ).first()
    
    def get_by_gallery_id(self, gallery_id: int) -> Optional[DetailHouse]:
        """Get a detail house by gallery ID"""
        return self.session.query(DetailHouse).filter(DetailHouse.gallery_id == gallery_id).first()
    
    def create(self, detail_data: Dict[str, Any], gallery_id: Optional[int] = None) -> DetailHouse:
        """Create a new detail house"""
        if gallery_id:
            detail_data['gallery_id'] = gallery_id
            
        # Extract floor plans if they exist
        floor_plans_data = detail_data.pop('floor_plans', None)
        
        detail_house = DetailHouse(**detail_data)
        self.session.add(detail_house)
        self.session.flush()  # Get ID without committing
        
        # Add floor plans if they exist
        if floor_plans_data and isinstance(floor_plans_data, list):
            for plan_data in floor_plans_data:
                plan = FloorPlan(house_id=detail_house.id, **plan_data)
                self.session.add(plan)
        
        self.session.commit()
        logger.info(f"Created detail house: {detail_house.address}, {detail_house.city}")
        return detail_house
    
    def update(self, detail_id: int, detail_data: Dict[str, Any]) -> Optional[DetailHouse]:
        """Update an existing detail house"""
        detail_house = self.get_by_id(detail_id)
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
            self.session.query(FloorPlan).filter(FloorPlan.house_id == detail_id).delete()
            
            # Add new floor plans
            for plan_data in floor_plans_data:
                plan = FloorPlan(house_id=detail_id, **plan_data)
                self.session.add(plan)
        
        self.session.commit()
        logger.info(f"Updated detail house: {detail_house.address}, {detail_house.city}")
        return detail_house
    
    def get_or_create(self, detail_data: Dict[str, Any], gallery_id: Optional[int] = None) -> DetailHouse:
        """Get an existing detail house or create a new one"""
        address = detail_data.get('address')
        postal_code = detail_data.get('postal_code')
        city = detail_data.get('city')
        
        if not all([address, postal_code, city]):
            raise ValueError("Address, postal code, and city are required for detail house")
        
        existing = None
        
        # Try to find by gallery_id if provided
        if gallery_id:
            existing = self.get_by_gallery_id(gallery_id)
        
        # If not found, try to find by address
        if not existing:
            existing = self.get_by_address(address, postal_code, city)
        
        if existing:
            # Update with new data
            return self.update(existing.id, detail_data)
        
        # Create new
        return self.create(detail_data, gallery_id)
    
    def delete(self, detail_id: int) -> bool:
        """Delete a detail house"""
        detail_house = self.get_by_id(detail_id)
        if not detail_house:
            return False
        
        # Floor plans will be automatically deleted due to cascade
        self.session.delete(detail_house)
        self.session.commit()
        logger.info(f"Deleted detail house with ID: {detail_id}")
        return True


class FloorPlanRepository:
    """Repository for FloorPlan operations"""
    
    def __init__(self, session: Optional[Session] = None):
        self.session = session or get_db_session()
    
    def get_by_id(self, plan_id: int) -> Optional[FloorPlan]:
        """Get a floor plan by ID"""
        return self.session.query(FloorPlan).filter(FloorPlan.id == plan_id).first()
    
    def get_by_house_id(self, house_id: int) -> List[FloorPlan]:
        """Get all floor plans for a house"""
        return self.session.query(FloorPlan).filter(FloorPlan.house_id == house_id).all()
    
    def create(self, plan_data: Dict[str, Any]) -> FloorPlan:
        """Create a new floor plan"""
        floor_plan = FloorPlan(**plan_data)
        self.session.add(floor_plan)
        self.session.commit()
        logger.info(f"Created floor plan for house ID: {floor_plan.house_id}")
        return floor_plan
    
    def update(self, plan_id: int, plan_data: Dict[str, Any]) -> Optional[FloorPlan]:
        """Update an existing floor plan"""
        floor_plan = self.get_by_id(plan_id)
        if not floor_plan:
            return None
        
        for key, value in plan_data.items():
            if hasattr(floor_plan, key):
                setattr(floor_plan, key, value)
        
        self.session.commit()
        logger.info(f"Updated floor plan with ID: {plan_id}")
        return floor_plan
    
    def delete(self, plan_id: int) -> bool:
        """Delete a floor plan"""
        floor_plan = self.get_by_id(plan_id)
        if not floor_plan:
            return False
        
        self.session.delete(floor_plan)
        self.session.commit()
        logger.info(f"Deleted floor plan with ID: {plan_id}")
        return True 