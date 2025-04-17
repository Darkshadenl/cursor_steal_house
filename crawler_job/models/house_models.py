from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class House(BaseModel):
    """
    Unified model for house information representing all property data in a single schema.
    """

    # Basic information
    address: str = Field(..., description="The complete address of the house")
    city: str = Field(..., description="The city where the house is located")
    postal_code: Optional[str] = Field(None, description="The postal code of the house")
    neighborhood: Optional[str] = Field(
        None, description="The neighborhood where the house is located"
    )

    # Status information
    status: str = Field(..., description="The status of the house, e.g. 'For rent'")
    high_demand: bool = Field(
        False, description="Indicates if the house has many viewing requests"
    )
    demand_message: Optional[str] = Field(
        None, description="Message about the popularity of the house"
    )

    # Detailed link
    detail_url: Optional[str] = Field(
        None, description="URL to the detail page of the house"
    )

    # Financial information
    rental_price: Optional[str] = Field(
        None, description="The monthly rental price in euros"
    )
    service_costs: Optional[str] = Field(None, description="Service costs in euros")

    # Income requirements
    min_income_single: Optional[str] = Field(
        None, description="Minimum income requirement for single person"
    )
    min_income_joint: Optional[str] = Field(
        None, description="Minimum income requirement for joint application"
    )
    read_more_url: Optional[str] = Field(
        None, description="Link to more information about income requirements"
    )

    # Features and details
    square_meters: Optional[int] = Field(
        None, description="The living area in square meters"
    )
    bedrooms: Optional[int] = Field(None, description="Number of bedrooms")
    energy_label: Optional[str] = Field(
        None, description="Energy label of the house (A, B, C, etc.)"
    )
    available_from: Optional[str] = Field(
        None, description="From when the house is available"
    )
    complex: Optional[str] = Field(
        None, description="Name of the complex the house belongs to"
    )

    # Descriptions
    description: Optional[str] = Field(
        None, description="General description of the house"
    )

    # Complex information
    complex_name: Optional[str] = Field(None, description="Name of the complex")
    complex_description: Optional[str] = Field(
        None, description="Description of the complex"
    )
    year_of_construction: Optional[int] = Field(
        None, description="Year the complex was built"
    )
    number_of_objects: Optional[str] = Field(
        None, description="Number of objects in the complex"
    )
    number_of_floors: Optional[str] = Field(
        None, description="Number of floors in the complex"
    )

    # Location information
    location_map_url: Optional[str] = Field(
        None, description="URL to the map with the location"
    )

    # Action links
    request_viewing_url: Optional[str] = Field(
        None, description="URL to request a viewing of the property"
    )

    # Extra options
    options: Optional[str] = Field(
        None, description="Extra options or possibilities for the house"
    )

    def to_db_model(self):
        """Convert House Pydantic model to DbHouse SQLAlchemy model

        Returns:
            DbHouse: Converted DbHouse SQLAlchemy model
        """
        from crawler_job.models.db_models import DbHouse

        return DbHouse(
            address=self.address,
            city=self.city,
            postal_code=self.postal_code,
            neighborhood=self.neighborhood,
            status=self.status,
            high_demand=self.high_demand,
            demand_message=self.demand_message,
            detail_url=self.detail_url,
            rental_price=self.rental_price,
            service_costs=self.service_costs,
            min_income_single=self.min_income_single,
            min_income_joint=self.min_income_joint,
            read_more_url=self.read_more_url,
            square_meters=self.square_meters,
            bedrooms=self.bedrooms,
            energy_label=self.energy_label,
            available_from=self.available_from,
            complex=self.complex,
            description=self.description,
            complex_name=self.complex_name,
            complex_description=self.complex_description,
            year_of_construction=self.year_of_construction,
            number_of_objects=self.number_of_objects,
            number_of_floors=self.number_of_floors,
            location_map_url=self.location_map_url,
            request_viewing_url=self.request_viewing_url,
            options=self.options,
        )

    @classmethod
    async def from_db_model_async(cls, db_model):
        """Convert DbHouse SQLAlchemy model to House Pydantic model

        Args:
            db_model: DbHouse SQLAlchemy model to convert

        Returns:
            House: Converted House Pydantic model
        """
        return cls(
            address=db_model.address,
            city=db_model.city,
            postal_code=db_model.postal_code,
            neighborhood=db_model.neighborhood,
            status=db_model.status,
            high_demand=db_model.high_demand,
            demand_message=db_model.demand_message,
            detail_url=db_model.detail_url,
            rental_price=db_model.rental_price,
            service_costs=db_model.service_costs,
            min_income_single=db_model.min_income_single,
            min_income_joint=db_model.min_income_joint,
            read_more_url=db_model.read_more_url,
            square_meters=db_model.square_meters,
            bedrooms=db_model.bedrooms,
            energy_label=db_model.energy_label,
            available_from=db_model.available_from,
            complex=db_model.complex,
            description=db_model.description,
            complex_name=db_model.complex_name,
            complex_description=db_model.complex_description,
            year_of_construction=db_model.year_of_construction,
            number_of_objects=db_model.number_of_objects,
            number_of_floors=db_model.number_of_floors,
            location_map_url=db_model.location_map_url,
            request_viewing_url=db_model.request_viewing_url,
            options=db_model.options,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a House instance from a dictionary

        Args:
            data: Dictionary containing house data

        Returns:
            House: New House Pydantic model created from the dictionary
        """
        return cls(
            address=data.get("address"),
            city=data.get("city"),
            postal_code=data.get("postal_code"),
            neighborhood=data.get("neighborhood"),
            status=data.get("status"),
            high_demand=data.get("high_demand", False),
            demand_message=data.get("demand_message"),
            detail_url=data.get("detail_url"),
            rental_price=data.get("rental_price"),
            service_costs=data.get("service_costs"),
            min_income_single=data.get("min_income_single"),
            min_income_joint=data.get("min_income_joint"),
            read_more_url=data.get("read_more_url"),
            square_meters=data.get("square_meters"),
            bedrooms=data.get("bedrooms"),
            energy_label=data.get("energy_label"),
            available_from=data.get("available_from"),
            complex=data.get("complex"),
            description=data.get("description"),
            complex_name=data.get("complex_name"),
            complex_description=data.get("complex_description"),
            year_of_construction=data.get("year_of_construction"),
            number_of_objects=data.get("number_of_objects"),
            number_of_floors=data.get("number_of_floors"),
            location_map_url=data.get("location_map_url"),
            request_viewing_url=data.get("request_viewing_url"),
            options=data.get("options"),
        )


class FetchedPage(BaseModel):
    """Model for a fetched page of data"""

    url: str = Field(..., description="The URL of the fetched page")
    markdown: str = Field(..., description="The markdown content of the fetched page")
    success: bool = Field(..., description="Whether the fetch was successful")


__all__ = [
    "House",
    "FetchedPage",
]
