from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class GalleryHouse(BaseModel):
    """Model for basic house information in gallery view"""

    # Address and location
    address: str = Field(
        ..., description="The address of the house, including house number"
    )
    city: str = Field(..., description="The city where the house is located")

    # Status
    status: str = Field(..., description="The status of the house, e.g. 'For rent'")

    # Media
    image_url: Optional[str] = Field(
        None, description="URL to the main image of the house"
    )

    # Metadata
    high_demand: bool = Field(
        False, description="Indicates if the house has many viewing requests"
    )
    demand_message: Optional[str] = Field(
        None, description="Message about the popularity of the house"
    )

    # Link
    detail_url: Optional[str] = Field(
        None, description="URL to the detail page of the house"
    )

    def to_db_model(self):
        """Convert GalleryHouse Pydantic model to DbGalleryHouse SQLAlchemy model"""
        from crawler_job.models.db_models import DbGalleryHouse

        # Check if demand_message indicates high demand
        high_demand = self.high_demand
        if (
            not high_demand
            and self.demand_message
            == "This house has many viewing requests. Increase you chance by selecting a different property."
        ):
            high_demand = True

        return DbGalleryHouse(
            address=self.address,
            city=self.city,
            status=self.status,
            image_url=self.image_url,
            high_demand=high_demand,
            demand_message=self.demand_message,
            detail_url=self.detail_url,
        )

    @classmethod
    async def from_db_model_async(cls, db_model):
        """Convert DbGalleryHouse SQLAlchemy model to GalleryHouse Pydantic model"""
        # Check if demand_message indicates high demand
        high_demand = db_model.high_demand
        if (
            not high_demand
            and db_model.demand_message
            == "This house has many viewing requests. Increase you chance by selecting a different property."
        ):
            high_demand = True

        return cls(
            address=db_model.address,
            city=db_model.city,
            status=db_model.status,
            image_url=db_model.image_url,
            high_demand=high_demand,
            demand_message=db_model.demand_message,
            detail_url=db_model.detail_url,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a GalleryHouse instance from a dictionary"""
        # Check if demand_message indicates high demand
        high_demand = data.get("high_demand", False)
        if (
            not high_demand
            and data.get("demand_message")
            == "This house has many viewing requests. Increase you chance by selecting a different property."
        ):
            high_demand = True

        return cls(
            address=data["address"],
            city=data["city"],
            status=data["status"],
            image_url=data.get("image_url"),
            high_demand=high_demand,
            demand_message=data.get("demand_message"),
            detail_url=data.get("detail_url"),
        )


class IncomeRequirement(BaseModel):
    """Model for income requirements"""

    min_income_single: Optional[str] = Field(
        None, description="Minimum income requirement for single person"
    )
    min_income_joint: Optional[str] = Field(
        None, description="Minimum income requirement for joint application"
    )
    read_more_url: Optional[str] = Field(
        None, description="Link to more information about income requirements"
    )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create an IncomeRequirement instance from a dictionary"""
        return cls(
            min_income_single=data.get("min_income_single"),
            min_income_joint=data.get("min_income_joint"),
            read_more_url=data.get("read_more_url"),
        )


class FloorPlan(BaseModel):
    """Model for floor plans"""

    image_url: Optional[str] = Field(None, description="URL to the floor plan image")
    description: Optional[str] = Field(
        None, description="Description of the floor plan"
    )

    def to_db_model(self, house_id: int):
        """Convert FloorPlan Pydantic model to DbFloorPlan SQLAlchemy model"""
        from crawler_job.models.db_models import DbFloorPlan

        return DbFloorPlan(
            house_id=house_id,
            image_url=self.image_url,
            description=self.description,
        )

    @classmethod
    async def from_db_model_async(cls, db_model):
        """Convert DbFloorPlan SQLAlchemy model to FloorPlan Pydantic model"""
        return cls(
            image_url=db_model.image_url,
            description=db_model.description,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a FloorPlan instance from a dictionary"""
        return cls(
            image_url=data.get("image_url"),
            description=data.get("description"),
        )


class ComplexInfo(BaseModel):
    """Model for complex information"""

    name: Optional[str] = Field(None, description="Name of the complex")
    description: Optional[str] = Field(None, description="Description of the complex")
    year_of_construction: Optional[int] = Field(
        None, description="Year the complex was built"
    )
    number_of_objects: Optional[str] = Field(
        None, description="Number of objects in the complex"
    )
    number_of_floors: Optional[str] = Field(
        None, description="Number of floors in the complex"
    )
    image_url: Optional[str] = Field(None, description="URL to image of the complex")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a ComplexInfo instance from a dictionary"""
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            year_of_construction=data.get("year_of_construction"),
            number_of_objects=data.get("number_of_objects"),
            number_of_floors=data.get("number_of_floors"),
            image_url=data.get("image_url"),
        )


class DetailHouse(BaseModel):
    """Model for detailed house information"""

    # Basic information
    address: str = Field(..., description="The complete address of the house")
    postal_code: str = Field(..., description="The postal code of the house")
    city: str = Field(..., description="The city where the house is located")
    neighborhood: Optional[str] = Field(
        None, description="The neighborhood where the house is located"
    )

    # Financial information
    rental_price: str = Field(..., description="The monthly rental price in euros")
    service_costs: Optional[str] = Field(None, description="Service costs in euros")
    income_requirements: Optional[IncomeRequirement] = Field(
        None, description="Income requirements for rent"
    )

    # Features and details
    square_meters: int = Field(..., description="The living area in square meters")
    bedrooms: int = Field(..., description="Number of bedrooms")
    energy_label: Optional[str] = Field(
        None, description="Energy label of the house (A, B, C, etc.)"
    )
    status: str = Field(
        ..., description="The status of the house (for rent, for sale, etc.)"
    )
    available_from: Optional[str] = Field(
        None, description="From when the house is available"
    )
    complex: Optional[str] = Field(
        None, description="Name of the complex the house belongs to"
    )

    # Descriptions
    description: str = Field(..., description="General description of the house")

    # Media
    # floor_plans: Optional[List[FloorPlan]] = Field(
    #     None, description="Floor plans of the house"
    # )

    # Complex information
    complex_info: Optional[ComplexInfo] = Field(
        None, description="Information about the complex"
    )

    # # Location information
    # location_map_url: Optional[str] = Field(
    #     None, description="URL to the map with the location"
    # )

    # Action links
    request_viewing_url: Optional[str] = Field(
        None, description="URL to request a viewing of the property"
    )

    # Extra options
    options: Optional[str] = Field(
        None, description="Extra options or possibilities for the house"
    )

    gallery_id: Optional[int] = Field(
        None, description="ID of the gallery model of this house"
    )

    def to_db_model(self):
        """Convert DetailHouse Pydantic model to DbDetailHouse SQLAlchemy model"""
        from crawler_job.models.db_models import DbDetailHouse

        db_house = DbDetailHouse(
            gallery_id=self.gallery_id,
            address=self.address,
            postal_code=self.postal_code,
            city=self.city,
            neighborhood=self.neighborhood,
            rental_price=self.rental_price,
            service_costs=self.service_costs,
            square_meters=self.square_meters,
            bedrooms=self.bedrooms,
            energy_label=self.energy_label,
            status=self.status,
            available_from=self.available_from,
            complex=self.complex,
            description=self.description,
            # location_map_url=self.location_map_url,
            request_viewing_url=self.request_viewing_url,
            options=self.options,
        )

        # Set income requirements if they exist
        if self.income_requirements:
            db_house.min_income_single = self.income_requirements.min_income_single
            db_house.min_income_joint = self.income_requirements.min_income_joint
            db_house.read_more_url = self.income_requirements.read_more_url

        # Set complex info if it exists
        if self.complex_info:
            db_house.complex_name = self.complex_info.name
            db_house.complex_description = self.complex_info.description
            db_house.year_of_construction = self.complex_info.year_of_construction
            db_house.number_of_objects = self.complex_info.number_of_objects
            db_house.number_of_floors = self.complex_info.number_of_floors
            db_house.complex_image_url = self.complex_info.image_url

        return db_house

    @classmethod
    async def from_db_model_async(cls, db_model):
        """Convert DbDetailHouse SQLAlchemy model to DetailHouse Pydantic model"""
        income_requirements = None
        if any(
            [
                db_model.min_income_single,
                db_model.min_income_joint,
                db_model.read_more_url,
            ]
        ):
            income_requirements = IncomeRequirement(
                min_income_single=db_model.min_income_single,
                min_income_joint=db_model.min_income_joint,
                read_more_url=db_model.read_more_url,
            )

        # Create complex info if it exists
        complex_info = None
        if any(
            [
                db_model.complex_name,
                db_model.complex_description,
                db_model.year_of_construction,
                db_model.number_of_objects,
                db_model.number_of_floors,
                db_model.complex_image_url,
            ]
        ):
            complex_info = ComplexInfo(
                name=db_model.complex_name,
                description=db_model.complex_description,
                year_of_construction=db_model.year_of_construction,
                number_of_objects=db_model.number_of_objects,
                number_of_floors=db_model.number_of_floors,
                image_url=db_model.complex_image_url,
            )

        return cls(
            address=db_model.address,
            postal_code=db_model.postal_code,
            city=db_model.city,
            neighborhood=db_model.neighborhood,
            rental_price=db_model.rental_price,
            service_costs=db_model.service_costs,
            square_meters=db_model.square_meters,
            bedrooms=db_model.bedrooms,
            energy_label=db_model.energy_label,
            status=db_model.status,
            available_from=db_model.available_from,
            complex=db_model.complex,
            description=db_model.description,
            location_map_url=db_model.location_map_url,
            request_viewing_url=db_model.request_viewing_url,
            options=db_model.options,
            income_requirements=income_requirements,
            complex_info=complex_info,
            # floor_plans=floor_plans if floor_plans else None,
            gallery_id=db_model.gallery_id,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a DetailHouse instance from a dictionary"""
        # Handle nested objects
        income_requirements = None
        if "income_requirements" in data and data["income_requirements"]:
            income_requirements = IncomeRequirement.from_dict(
                data["income_requirements"]
            )

        complex_info = None
        if "complex_info" in data and data["complex_info"]:
            complex_info = ComplexInfo.from_dict(data["complex_info"])

        # floor_plans = None
        # if "floor_plans" in data and data["floor_plans"]:
        #     floor_plans = [FloorPlan.from_dict(plan) for plan in data["floor_plans"]]

        return cls(
            address=data["address"],
            postal_code=data["postal_code"],
            city=data["city"],
            neighborhood=data.get("neighborhood"),
            rental_price=data["rental_price"],
            service_costs=data.get("service_costs"),
            income_requirements=income_requirements,
            square_meters=data["square_meters"],
            bedrooms=data["bedrooms"],
            energy_label=data.get("energy_label"),
            status=data["status"],
            available_from=data.get("available_from"),
            complex=data.get("complex"),
            description=data["description"],
            # floor_plans=floor_plans,
            complex_info=complex_info,
            location_map_url=data.get("location_map_url"),
            request_viewing_url=data.get("request_viewing_url"),
            options=data.get("options"),
            gallery_id=data.get("gallery_id"),
        )


class FetchedPage(BaseModel):
    """Model for a fetched property page with its content and extraction results"""

    url: str = Field(..., description="The URL of the fetched page")
    markdown: str = Field(..., description="The raw markdown content of the page")
    success: bool = Field(..., description="Whether the page was successfully fetched")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a FetchedPage instance from a dictionary"""
        return cls(url=data["url"], markdown=data["markdown"], success=data["success"])


__all__ = [
    "GalleryHouse",
    "DetailHouse",
    "IncomeRequirement",
    "FloorPlan",
    "ComplexInfo",
    "FetchedPage",
]
