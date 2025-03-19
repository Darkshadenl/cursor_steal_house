from typing import Dict, Any, List, Optional
import logging
from sqlalchemy.orm import Session
from contextlib import contextmanager

from .repositories import GalleryHouseRepository, DetailHouseRepository, FloorPlanRepository
from .transformers import GalleryHouseTransformer, DetailHouseTransformer
from .db_connection import get_db_session

logger = logging.getLogger(__name__)

@contextmanager
def get_repositories(session=None):
    """Context manager to get all repositories with a shared session"""
    session = session or get_db_session()
    try:
        yield {
            'gallery': GalleryHouseRepository(session),
            'detail': DetailHouseRepository(session),
            'floor_plan': FloorPlanRepository(session)
        }
    finally:
        session.close()

class HouseService:
    """Service for handling house data storage"""
    
    def __init__(self, session: Optional[Session] = None):
        """Initialize with optional session"""
        self.session = session or get_db_session()
    
    def store_gallery_houses(self, gallery_houses: List[Dict[str, Any]]) -> List[int]:
        """Store a list of gallery houses and return their IDs"""
        gallery_ids = []
        
        with get_repositories(self.session) as repos:
            for house_data in gallery_houses:
                try:
                    # Transform data
                    db_data = GalleryHouseTransformer.from_dict(house_data)
                    
                    # Store in database
                    gallery_house = repos['gallery'].get_or_create(db_data)
                    gallery_ids.append(gallery_house.id)
                    
                    logger.info(f"Stored gallery house: {gallery_house.address}, {gallery_house.city}")
                except Exception as e:
                    logger.error(f"Error storing gallery house: {str(e)}")
        
        return gallery_ids
    
    def store_detail_house(self, detail_house: Dict[str, Any], gallery_id: Optional[int] = None) -> Optional[int]:
        """Store a detail house and return its ID"""
        with get_repositories(self.session) as repos:
            try:
                # Transform data
                db_data = DetailHouseTransformer.from_dict(detail_house, gallery_id)
                
                # Store in database
                detail_house_obj = repos['detail'].get_or_create(db_data, gallery_id)
                
                logger.info(f"Stored detail house: {detail_house_obj.address}, {detail_house_obj.city}")
                return detail_house_obj.id
            except Exception as e:
                logger.error(f"Error storing detail house: {str(e)}")
                return None
    
    def store_crawler_results(self, gallery_data: List[Dict[str, Any]], detail_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Store crawler results including gallery and detail data"""
        result = {
            'gallery_ids': [],
            'detail_id': None,
            'success': False
        }
        
        try:
            # Store gallery houses
            if gallery_data:
                gallery_ids = self.store_gallery_houses(gallery_data)
                result['gallery_ids'] = gallery_ids
                logger.info(f"Stored {len(gallery_ids)} gallery houses")
            
            # Store detail house if available
            if detail_data:
                # If we have gallery data, link to the last gallery house
                gallery_id = result['gallery_ids'][-1] if result['gallery_ids'] else None
                
                detail_id = self.store_detail_house(detail_data, gallery_id)
                result['detail_id'] = detail_id
                
                if detail_id:
                    logger.info(f"Stored detail house with ID: {detail_id}")
            
            result['success'] = True
        except Exception as e:
            logger.error(f"Error in store_crawler_results: {str(e)}")
            result['error'] = str(e)
        
        return result 