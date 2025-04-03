from typing import List, Optional, Dict, Any
import logging

# Import Pydantic models
from crawler_job.models.house_models import (
    GalleryHouse as PydanticGalleryHouse,
)
from crawler_job.models.house_models import (
    DetailHouse as PydanticDetailHouse,
)
from crawler_job.models.house_models import (
    FloorPlan as PydanticFloorPlan,
)
from ..models.db_models import (
    DbGalleryHouse as DBGalleryHouse,
    DbDetailHouse as DBDetailHouse,
    DbFloorPlan as DBFloorPlan,
)

logger = logging.getLogger(__name__)


class GalleryHouseTransformer:
    """Transforms between GalleryHouse models and their representations"""

    @staticmethod
    def dict_to_pydantic(data: Dict[str, Any]) -> PydanticGalleryHouse:
        """Convert dictionary to GalleryHouse Pydantic model"""
        return PydanticGalleryHouse(**data)

    @staticmethod
    def pydantic_to_dict(house: PydanticGalleryHouse) -> Dict[str, Any]:
        """Convert GalleryHouse Pydantic model to dictionary"""
        return house.model_dump()

    @staticmethod
    def pydantic_to_db(house: PydanticGalleryHouse) -> DBGalleryHouse:
        """Convert GalleryHouse Pydantic model to DB model"""
        return DBGalleryHouse(
            address=house.address,
            city=house.city,
            status=house.status,
            image_url=house.image_url,
            high_demand=house.high_demand,
            demand_message=house.demand_message,
            detail_url=house.detail_url,
        )

    @staticmethod
    def db_to_pydantic(db_house: DBGalleryHouse) -> PydanticGalleryHouse:
        """Convert DB model to GalleryHouse Pydantic model"""
        return PydanticGalleryHouse(
            address=db_house.address,
            city=db_house.city,
            status=db_house.status,
            image_url=db_house.image_url,
            high_demand=db_house.high_demand,
            demand_message=db_house.demand_message,
            detail_url=db_house.detail_url,
        )


class FloorPlanTransformer:
    """Transforms between FloorPlan models and their representations"""

    @staticmethod
    def dict_to_pydantic(data: Dict[str, Any]) -> PydanticFloorPlan:
        """Convert dictionary to FloorPlan Pydantic model"""
        return PydanticFloorPlan(**data)

    @staticmethod
    def pydantic_to_dict(plan: PydanticFloorPlan) -> Dict[str, Any]:
        """Convert FloorPlan Pydantic model to dictionary"""
        return plan.model_dump()

    @staticmethod
    def pydantic_to_db(plan: PydanticFloorPlan, house_id: int) -> DBFloorPlan:
        """Convert FloorPlan Pydantic model to DB model"""
        return DBFloorPlan(
            house_id=house_id, image_url=plan.image_url, description=plan.description
        )

    @staticmethod
    def db_to_pydantic(db_plan: DBFloorPlan) -> PydanticFloorPlan:
        """Convert DB model to FloorPlan Pydantic model"""
        return PydanticFloorPlan(
            image_url=db_plan.image_url, description=db_plan.description
        )


class DetailHouseTransformer:
    """Transforms between DetailHouse models and their representations"""

    @staticmethod
    def dict_to_pydantic(data: Dict[str, Any]) -> PydanticDetailHouse:
        """Convert dictionary to DetailHouse Pydantic model"""
        return PydanticDetailHouse(**data)

    @staticmethod
    def pydantic_to_dict(house: PydanticDetailHouse) -> Dict[str, Any]:
        """Convert DetailHouse Pydantic model to dictionary"""
        return house.model_dump()

    @staticmethod
    def pydantic_to_db(house: PydanticDetailHouse) -> DBDetailHouse:
        """Convert DetailHouse Pydantic model to DB model"""
        db_house = DBDetailHouse(
            gallery_id=house.gallery_id,
            address=house.address,
            postal_code=house.postal_code,
            city=house.city,
            neighborhood=house.neighborhood,
            rental_price=house.rental_price,
            service_costs=house.service_costs,
            square_meters=house.square_meters,
            bedrooms=house.bedrooms,
            energy_label=house.energy_label,
            status=house.status,
            available_from=house.available_from,
            complex=house.complex,
            description=house.description,
            location_map_url=house.location_map_url,
            request_viewing_url=house.request_viewing_url,
            options=house.options,
        )

        # Set income requirements if they exist
        if house.income_requirements:
            db_house.min_income_single = house.income_requirements.min_income_single
            db_house.min_income_joint = house.income_requirements.min_income_joint
            db_house.read_more_url = house.income_requirements.read_more_url

        # Set complex info if it exists
        if house.complex_info:
            db_house.complex_name = house.complex_info.name
            db_house.complex_description = house.complex_info.description
            db_house.year_of_construction = house.complex_info.year_of_construction
            db_house.number_of_objects = house.complex_info.number_of_objects
            db_house.number_of_floors = house.complex_info.number_of_floors
            db_house.complex_image_url = house.complex_info.image_url

        return db_house

    @staticmethod
    def db_to_pydantic(db_house: DBDetailHouse) -> PydanticDetailHouse:
        """Convert DB model to DetailHouse Pydantic model"""
        # Create floor plans list
        floor_plans = []
        if hasattr(db_house, "floor_plans"):
            for plan in db_house.floor_plans:
                floor_plans.append(
                    PydanticFloorPlan(
                        image_url=plan.image_url, description=plan.description
                    )
                )

        # Create income requirements if they exist
        income_requirements = None
        if any(
            [
                db_house.min_income_single,
                db_house.min_income_joint,
                db_house.read_more_url,
            ]
        ):
            income_requirements = {
                "min_income_single": db_house.min_income_single,
                "min_income_joint": db_house.min_income_joint,
                "read_more_url": db_house.read_more_url,
            }

        # Create complex info if it exists
        complex_info = None
        if any(
            [
                db_house.complex_name,
                db_house.complex_description,
                db_house.year_of_construction,
                db_house.number_of_objects,
                db_house.number_of_floors,
                db_house.complex_image_url,
            ]
        ):
            complex_info = {
                "name": db_house.complex_name,
                "description": db_house.complex_description,
                "year_of_construction": db_house.year_of_construction,
                "number_of_objects": db_house.number_of_objects,
                "number_of_floors": db_house.number_of_floors,
                "image_url": db_house.complex_image_url,
            }

        return PydanticDetailHouse(
            address=db_house.address,
            postal_code=db_house.postal_code,
            city=db_house.city,
            neighborhood=db_house.neighborhood,
            rental_price=db_house.rental_price,
            service_costs=db_house.service_costs,
            square_meters=db_house.square_meters,
            bedrooms=db_house.bedrooms,
            energy_label=db_house.energy_label,
            status=db_house.status,
            available_from=db_house.available_from,
            complex=db_house.complex,
            description=db_house.description,
            location_map_url=db_house.location_map_url,
            request_viewing_url=db_house.request_viewing_url,
            options=db_house.options,
            income_requirements=income_requirements,
            complex_info=complex_info,
            floor_plans=floor_plans,
        )
