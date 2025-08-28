from typing import Dict, List, Optional, Any

from pydantic import BaseModel, ConfigDict, Field
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


# Pydantic models for configuration data
class GalleryExtractionConfig(BaseModel):
    """
    Pydantic model for gallery extraction configuration.
    """

    correct_urls_paths: Optional[List[str]] = None
    gallery_container_selector: Optional[str] = None
    schema: Optional[Dict[str, Any]] = None
    schema_type: Optional[str] = "xpath" or "css"
    regex: Optional[str] = None
    extra_llm_instructions: Optional[str] = None
    next_page_selector: Optional[str] = None
    next_page_xpath: Optional[str] = None
    ignore_domains: Optional[List[str]] = None

    model_config = ConfigDict(from_attributes=True)


class DetailPageExtractionConfig(BaseModel):
    """
    Pydantic model for detail page extraction configuration.
    """

    schema_type: str = "xpath" or "css" or "llm"
    schema: Optional[Dict[str, Any]] = None
    detail_container_selector: Optional[str] = None
    extra_llm_instructions: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
    ignore_domains: Optional[List[str]] = None


class SitemapExtractionConfig(BaseModel):
    """
    Pydantic model for sitemap extraction configuration.
    """

    schema: Optional[Dict[str, Any]] = None
    regex: Optional[str] = None
    extra_llm_instructions: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class NavigationConfig(BaseModel):
    """
    Pydantic model for navigation configuration.
    """

    sitemap: Optional[str] = None
    gallery: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class FilteringConfig(BaseModel):
    """
    Pydantic model for filtering configuration.
    """

    filters_container_selector: Optional[str] = None
    js_code: Optional[str] = None
    filter_url_suffix: Optional[str] = None
    cities: Optional[List[str]] = None

    model_config = ConfigDict(from_attributes=True)


class LoginConfig(BaseModel):
    """
    Pydantic model for login configuration.
    """

    login_url_path: Optional[str] = None
    login_url: Optional[str] = None
    username_selector: str
    password_selector: str
    submit_selector: str
    success_check_url_path: Optional[str] = None
    expected_url_path: Optional[str] = None
    expected_url: Optional[str] = None
    success_indicator_selector: Optional[str] = None
    validate_login: bool = True
    login_required: bool = True

    model_config = ConfigDict(from_attributes=True)


class CookiesConfig(BaseModel):
    """
    Pydantic model for cookies configuration.
    """

    accept_cookies_selector: Optional[str] = None


class StrategyConfig(BaseModel):
    """
    Pydantic model for strategy configuration.
    """

    navigation_config: NavigationConfig
    cookies_config: Optional[CookiesConfig] = None
    filtering_config: Optional[FilteringConfig] = None
    gallery_extraction_config: Optional[GalleryExtractionConfig] = None
    detail_page_extraction_config: Optional[DetailPageExtractionConfig] = None
    sitemap_extraction_config: Optional[SitemapExtractionConfig] = None
    login_config: Optional[LoginConfig] = None

    model_config = ConfigDict(from_attributes=True)


class WebsiteConfig(BaseModel):
    id: int
    name: str
    base_url: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class WebsiteScrapeConfigJson(BaseModel):
    """
    Pydantic model for the complete website configuration.
    """

    website_name: str
    scrape_strategy: str = "gallery" or "sitemap"
    strategy_config: StrategyConfig
    session_id: str
    website_info: WebsiteConfig

    model_config = ConfigDict(from_attributes=True)


class ExtractionConfig(BaseModel):
    """
    Pydantic model for extraction configuration.
    """

    id: int
    website_id: int
    scope: str  # 'gallery' or 'detail'
    extraction_method: str = "css"  # 'css', 'xpath', or 'llm'
    llm_provider: Optional[str] = None
    llm_instruction: Optional[str] = None
    base_selector: Optional[str] = None
    field_mappings: Optional[List["FieldMapping"]] = None

    model_config = ConfigDict(from_attributes=True)


class FieldMapping(BaseModel):
    """
    Pydantic model for field mapping.
    """

    id: int
    extraction_config_id: int
    pydantic_field_name: str
    selector: str
    selector_type: str = "css"  # 'css' or 'xpath'
    extraction_type: str = "text"  # 'text', 'attribute', or 'html'
    attribute_name: Optional[str] = None
    is_required: bool = False
    default_value: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# Resolve forward references
WebsiteScrapeConfigJson.model_rebuild()
StrategyConfig.model_rebuild()


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
        None,
        description="URL to the detail page of the house. Should be the FULL url. Not just the relative path.",
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

    is_parkingspot: bool = Field(
        False, description="Indicates if this property is a parking spot"
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
            is_parkingspot=self.is_parkingspot,
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
            is_parkingspot=getattr(db_model, "is_parkingspot", False),
        )

    @classmethod
    def _pre_process_data(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pre-process the input data dictionary to ensure correct types and values for House fields.

        Args:
            data (Dict[str, Any]): Raw house data.

        Returns:
            Dict[str, Any]: Processed house data with correct types.
        """
        processed_data = data.copy()

        # Process bedrooms field
        try:
            if (
                "bedrooms" in data
                and data["bedrooms"] is not None
                and data["bedrooms"] != ""
            ):
                if not isinstance(data["bedrooms"], int):
                    processed_data["bedrooms"] = int(str(data["bedrooms"]).strip())
                else:
                    processed_data["bedrooms"] = data["bedrooms"]
        except (ValueError, TypeError):
            logger.warning(f"Could not convert bedrooms to int: {data.get('bedrooms')}")
            processed_data["bedrooms"] = None

        # Process area field to square_meters
        try:
            area_value = None
            if "area" in data and data["area"] is not None and data["area"] != "":
                if isinstance(data["area"], int):
                    area_value = data["area"]
                else:
                    area_str = (
                        str(data.get("area", ""))
                        .replace("m2", "")
                        .replace("m²", "")
                        .strip()
                    )
                    if area_str:
                        area_value = int(area_str)
            elif (
                "square_meters" in data
                and data["square_meters"] is not None
                and data["square_meters"] != ""
            ):
                if isinstance(data["square_meters"], int):
                    area_value = data["square_meters"]
                else:
                    area_str = (
                        str(data.get("square_meters", ""))
                        .replace("m2", "")
                        .replace("m²", "")
                        .strip()
                    )
                    if area_str:
                        area_value = int(area_str)
            if area_value is not None:
                processed_data["square_meters"] = area_value
        except (ValueError, TypeError):
            logger.warning(
                f"Could not convert area to int: {data.get('area') or data.get('square_meters')}"
            )
            processed_data["square_meters"] = None

        # Rename price to rental_price if present
        if "price" in processed_data:
            processed_data["rental_price"] = processed_data.pop("price")

        # Check if demand message indicates high demand
        demand_message = processed_data.get("demand_message")
        high_demand = False
        if (
            demand_message
            and isinstance(demand_message, str)
            and any(
                keyword in demand_message.lower()
                for keyword in ["hoge interesse", "veel interesse", "popular"]
            )
        ):
            high_demand = True
        processed_data["high_demand"] = high_demand

        return processed_data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a House instance from a dictionary

        Also processes data to ensure correct types and values.

        Args:
            data: Dictionary containing house data

        Returns:
            House: New House Pydantic model created from the dictionary
        """
        data = cls._pre_process_data(data)

        return cls(
            address=data.get("address", ""),
            city=data.get("city", ""),
            postal_code=data.get("postal_code", ""),
            neighborhood=data.get("neighborhood", ""),
            status=data.get("status", ""),
            high_demand=data.get("high_demand", False),
            demand_message=data.get("demand_message", ""),
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
            is_parkingspot=data.get("is_parkingspot", False),
        )

    def to_readable_string(self) -> str:
        """Convert the house model to a human-readable string representation.
        Only includes fields that have values (not None).

        Returns:
            str: A formatted string with key-value pairs of house information
        """
        # Get all fields that have values
        fields = {k: str(v) for k, v in self.model_dump().items() if v is not None}

        # Create formatted string with each field on a new line
        return "\n".join(f"{k}: {v}" for k, v in fields.items())


class FetchedPage(BaseModel):
    """Model for a fetched page of data"""

    url: str = Field(..., description="The URL of the fetched page")
    markdown: str = Field(..., description="The markdown content of the fetched page")
    success: bool = Field(..., description="Whether the fetch was successful")


__all__ = [
    "WebsiteScrapeConfigJson",
    "WebsiteConfig",
    "LoginConfig",
    "NavigationConfig",
    "ExtractionConfig",
    "FieldMapping",
    "GalleryExtractionConfig",
    "DetailPageExtractionConfig",
    "FilteringConfig",
    "StrategyConfig",
    "House",
    "FetchedPage",
]
