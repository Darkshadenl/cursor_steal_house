from pydantic import BaseModel, Field
from typing import Optional, List
from python_scripts.db_models.models import GalleryHouse as DBGalleryHouse

class GalleryHouse(BaseModel):
    """Model for basic house information in gallery view"""
    
    # Address and location
    address: str = Field(..., description="The address of the house, including house number")
    city: str = Field(..., description="The city where the house is located")
    
    # Status
    status: str = Field(..., description="The status of the house, e.g. 'For rent'")
    
    # Media
    image_url: Optional[str] = Field(None, description="URL to the main image of the house")
    
    # Metadata
    high_demand: bool = Field(False, description="Indicates if the house has many viewing requests")
    demand_message: Optional[str] = Field(None, description="Message about the popularity of the house")
    
    # Link
    detail_url: Optional[str] = Field(None, description="URL to the detail page of the house")

class IncomeRequirement(BaseModel):
    """Model for income requirements"""
    min_income_single: str = Field(..., description="Minimum income requirement for single person")
    min_income_joint: Optional[str] = Field(None, description="Minimum income requirement for joint application")
    read_more_url: Optional[str] = Field(None, description="Link to more information about income requirements")

class FloorPlan(BaseModel):
    """Model for floor plans"""
    image_url: str = Field(..., description="URL to the floor plan image")
    description: Optional[str] = Field(None, description="Description of the floor plan")

class ComplexInfo(BaseModel):
    """Model for complex information"""
    name: str = Field(..., description="Name of the complex")
    description: str = Field(..., description="Description of the complex")
    year_of_construction: int = Field(..., description="Year the complex was built")
    number_of_objects: str = Field(..., description="Number of objects in the complex")
    number_of_floors: str = Field(..., description="Number of floors in the complex")
    image_url: Optional[str] = Field(None, description="URL to image of the complex")

class DetailHouse(BaseModel):
    """Model for detailed house information"""
    
    # Basic information
    address: str = Field(..., description="The complete address of the house")
    postal_code: str = Field(..., description="The postal code of the house")
    city: str = Field(..., description="The city where the house is located")
    neighborhood: Optional[str] = Field(None, description="The neighborhood where the house is located")
    
    # Financial information
    rental_price: str = Field(..., description="The monthly rental price in euros")
    service_costs: Optional[str] = Field(None, description="Service costs in euros")
    income_requirements: Optional[IncomeRequirement] = Field(None, description="Income requirements for rent")
    
    # Features and details
    square_meters: int = Field(..., description="The living area in square meters")
    bedrooms: int = Field(..., description="Number of bedrooms")
    energy_label: Optional[str] = Field(None, description="Energy label of the house (A, B, C, etc.)")
    status: str = Field(..., description="The status of the house (for rent, for sale, etc.)")
    available_from: Optional[str] = Field(None, description="From when the house is available")
    complex: Optional[str] = Field(None, description="Name of the complex the house belongs to")
    
    # Descriptions
    description: str = Field(..., description="General description of the house")
    
    # Media
    floor_plans: Optional[List[FloorPlan]] = Field(None, description="Floor plans of the house")
    
    # Complex information
    complex_info: Optional[ComplexInfo] = Field(None, description="Information about the complex")
    
    # Location information
    location_map_url: Optional[str] = Field(None, description="URL to the map with the location")
    
    # Action links
    request_viewing_url: Optional[str] = Field(None, description="URL to request a viewing of the property")
    
    # Extra options
    options: Optional[str] = Field(None, description="Extra options or possibilities for the house")
    
    gallery_id: Optional[int] = Field(None, description="ID of the gallery model of this house")

class FetchedPage(BaseModel):
    """Model for a fetched property page with its content and extraction results"""
    url: str = Field(..., description="The URL of the fetched page")
    markdown: str = Field(..., description="The raw markdown content of the page")
    success: bool = Field(..., description="Whether the page was successfully fetched")
    

__all__ = [
    'GalleryHouse',
    'DetailHouse',
    'IncomeRequirement',
    'FloorPlan',
    'ComplexInfo',
    'FetchedPage'
]
