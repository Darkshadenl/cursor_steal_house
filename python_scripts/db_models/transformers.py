from typing import Dict, Any, List, Optional
import logging

# Import Pydantic models
from python_scripts.crawlers.vesteda_models.house_models import GalleryHouse as PydanticGalleryHouse
from python_scripts.crawlers.vesteda_models.house_models import DetailHouse as PydanticDetailHouse
from python_scripts.crawlers.vesteda_models.house_models import FloorPlan as PydanticFloorPlan

logger = logging.getLogger(__name__)

class GalleryHouseTransformer:
    """Transforms gallery house data from crawler to database format"""
    
    @staticmethod
    def to_db_model(gallery_house: PydanticGalleryHouse) -> Dict[str, Any]:
        """Transform Pydantic GalleryHouse to database model dict"""
        return {
            'address': gallery_house.address,
            'city': gallery_house.city,
            'status': gallery_house.status,
            'image_url': gallery_house.image_url,
            'high_demand': gallery_house.high_demand,
            'demand_message': gallery_house.demand_message,
            'detail_url': gallery_house.detail_url
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Dict[str, Any]:
        """Transform raw dictionary data to database model dict"""
        return {
            'address': data.get('address', ''),
            'city': data.get('city', ''),
            'status': data.get('status', ''),
            'image_url': data.get('image_url'),
            'high_demand': data.get('high_demand', False),
            'demand_message': data.get('demand_message'),
            'detail_url': data.get('detail_url')
        }


class FloorPlanTransformer:
    """Transforms floor plan data from crawler to database format"""
    
    @staticmethod
    def to_db_model(floor_plan: PydanticFloorPlan, house_id: Optional[int] = None) -> Dict[str, Any]:
        """Transform Pydantic FloorPlan to database model dict"""
        model_dict = {
            'image_url': floor_plan.image_url,
            'description': floor_plan.description
        }
        
        if house_id:
            model_dict['house_id'] = house_id
            
        return model_dict
    
    @staticmethod
    def from_dict(data: Dict[str, Any], house_id: Optional[int] = None) -> Dict[str, Any]:
        """Transform raw dictionary data to database model dict"""
        model_dict = {
            'image_url': data.get('image_url', ''),
            'description': data.get('description')
        }
        
        if house_id:
            model_dict['house_id'] = house_id
            
        return model_dict
    
    @staticmethod
    def transform_list(floor_plans: List[Dict[str, Any]], house_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Transform a list of floor plans"""
        return [FloorPlanTransformer.from_dict(plan, house_id) for plan in floor_plans]


class DetailHouseTransformer:
    """Transforms detail house data from crawler to database format"""
    
    @staticmethod
    def to_db_model(detail_house: PydanticDetailHouse, gallery_id: Optional[int] = None) -> Dict[str, Any]:
        """Transform Pydantic DetailHouse to database model dict"""
        # Basic model data
        model_dict = {
            'address': detail_house.address,
            'postal_code': detail_house.postal_code,
            'city': detail_house.city,
            'neighborhood': detail_house.neighborhood,
            'rental_price': detail_house.rental_price,
            'service_costs': detail_house.service_costs,
            'square_meters': detail_house.square_meters,
            'bedrooms': detail_house.bedrooms,
            'energy_label': detail_house.energy_label,
            'status': detail_house.status,
            'available_from': detail_house.available_from,
            'complex': detail_house.complex,
            'description': detail_house.description,
            'location_map_url': detail_house.location_map_url,
            'options': detail_house.options
        }
        
        # Add gallery_id if provided
        if gallery_id:
            model_dict['gallery_id'] = gallery_id
        
        # Income requirements
        if detail_house.income_requirements:
            model_dict['min_income_single'] = detail_house.income_requirements.min_income_single
            model_dict['min_income_joint'] = detail_house.income_requirements.min_income_joint
            model_dict['read_more_url'] = detail_house.income_requirements.read_more_url
        
        # Complex information
        if detail_house.complex_info:
            model_dict['complex_name'] = detail_house.complex_info.name
            model_dict['complex_description'] = detail_house.complex_info.description
            model_dict['year_of_construction'] = detail_house.complex_info.year_of_construction
            model_dict['number_of_objects'] = detail_house.complex_info.number_of_objects
            model_dict['number_of_floors'] = detail_house.complex_info.number_of_floors
            model_dict['complex_image_url'] = detail_house.complex_info.image_url
        
        # Floor plans
        if detail_house.floor_plans:
            floor_plans = []
            for plan in detail_house.floor_plans:
                floor_plans.append(FloorPlanTransformer.to_db_model(plan))
            model_dict['floor_plans'] = floor_plans
        
        return model_dict
    
    @staticmethod
    def from_dict(data: Dict[str, Any], gallery_id: Optional[int] = None) -> Dict[str, Any]:
        """Transform raw dictionary data to database model dict"""
        # Basic model data
        model_dict = {
            'address': data.get('address', ''),
            'postal_code': data.get('postal_code', ''),
            'city': data.get('city', ''),
            'neighborhood': data.get('neighborhood'),
            'rental_price': data.get('rental_price', ''),
            'service_costs': data.get('service_costs'),
            'square_meters': data.get('square_meters', 0),
            'bedrooms': data.get('bedrooms', 0),
            'energy_label': data.get('energy_label'),
            'status': data.get('status', ''),
            'available_from': data.get('available_from'),
            'complex': data.get('complex'),
            'description': data.get('description', ''),
            'location_map_url': data.get('location_map_url'),
            'options': data.get('options')
        }
        
        # Add gallery_id if provided
        if gallery_id:
            model_dict['gallery_id'] = gallery_id
        
        # Income requirements
        income_requirements = data.get('income_requirements')
        if income_requirements:
            model_dict['min_income_single'] = income_requirements.get('min_income_single')
            model_dict['min_income_joint'] = income_requirements.get('min_income_joint')
            model_dict['read_more_url'] = income_requirements.get('read_more_url')
        
        # Complex information
        complex_info = data.get('complex_info')
        if complex_info:
            model_dict['complex_name'] = complex_info.get('name')
            model_dict['complex_description'] = complex_info.get('description')
            model_dict['year_of_construction'] = complex_info.get('year_of_construction')
            model_dict['number_of_objects'] = complex_info.get('number_of_objects')
            model_dict['number_of_floors'] = complex_info.get('number_of_floors')
            model_dict['complex_image_url'] = complex_info.get('image_url')
        
        # Floor plans
        floor_plans = data.get('floor_plans')
        if floor_plans and isinstance(floor_plans, list):
            model_dict['floor_plans'] = FloorPlanTransformer.transform_list(floor_plans)
        
        return model_dict 