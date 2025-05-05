from typing import Dict, List, Optional, Any

from pydantic import BaseModel, ConfigDict
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Text,
    TIMESTAMP,
    JSON,
    func,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

# Import the Base from db_models to ensure consistent base
from crawler_job.models.db_models import Base


class DbWebsite(Base):
    """
    SQLAlchemy model for website configurations.
    """

    __tablename__ = "websites"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    base_url = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationships
    login_config = relationship(
        "DbLoginConfig",
        back_populates="website",
        uselist=False,
        cascade="all, delete-orphan",
    )
    navigation_config = relationship(
        "DbNavigationConfig",
        back_populates="website",
        uselist=False,
        cascade="all, delete-orphan",
    )
    extraction_configs = relationship(
        "DbExtractionConfig", back_populates="website", cascade="all, delete-orphan"
    )


class DbWebsiteScrapeConfig(Base):
    """SQLAlchemy model for storing website scraping configurations in JSON format."""

    __tablename__ = "website_scrape_configs"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    website_identifier = Column(
        Integer, ForeignKey("steal_house.websites.id"), unique=True, nullable=False
    )
    config_json = Column(JSON, nullable=False)
    version = Column(Integer, nullable=True, default=1)
    is_enabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class DbLoginConfig(Base):
    """
    SQLAlchemy model for login configurations.
    """

    __tablename__ = "login_configs"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)
    website_id = Column(
        Integer,
        ForeignKey("steal_house.websites.id", ondelete="CASCADE"),
        nullable=False,
    )
    login_url_path = Column(String(255), nullable=True)
    username_selector = Column(String(255), nullable=False)
    password_selector = Column(String(255), nullable=False)
    submit_selector = Column(String(255), nullable=False)
    success_indicator_selector = Column(String(255), nullable=True)
    success_check_url = Column(String(255), nullable=True)
    credential_source = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationships
    website = relationship("DbWebsite", back_populates="login_config")


class DbNavigationConfig(Base):
    """
    SQLAlchemy model for navigation configurations.
    """

    __tablename__ = "navigation_configs"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)
    website_id = Column(
        Integer,
        ForeignKey("steal_house.websites.id", ondelete="CASCADE"),
        nullable=False,
    )
    gallery_url_path = Column(String(255), nullable=False)
    steps = Column(JSON, nullable=True)
    next_page_selector = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationships
    website = relationship("DbWebsite", back_populates="navigation_config")


class DbExtractionConfig(Base):
    """
    SQLAlchemy model for extraction configurations.
    """

    __tablename__ = "extraction_configs"
    __table_args__ = (
        UniqueConstraint(
            "website_id", "scope", name="uix_extraction_config_website_scope"
        ),
        {"schema": "steal_house"},
    )

    id = Column(Integer, primary_key=True)
    website_id = Column(
        Integer,
        ForeignKey("steal_house.websites.id", ondelete="CASCADE"),
        nullable=False,
    )
    scope = Column(String(50), nullable=False)  # 'gallery' or 'detail'
    extraction_method = Column(String(20), default="css")  # 'css', 'xpath', or 'llm'
    llm_provider = Column(String(50), nullable=True)
    llm_instruction = Column(Text, nullable=True)
    base_selector = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationships
    website = relationship("DbWebsite", back_populates="extraction_configs")
    field_mappings = relationship(
        "DbFieldMapping",
        back_populates="extraction_config",
        cascade="all, delete-orphan",
    )


class DbFieldMapping(Base):
    """
    SQLAlchemy model for field mappings.
    """

    __tablename__ = "field_mappings"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)
    extraction_config_id = Column(
        Integer,
        ForeignKey("steal_house.extraction_configs.id", ondelete="CASCADE"),
        nullable=False,
    )
    pydantic_field_name = Column(String(100), nullable=False)
    selector = Column(String(255), nullable=False)
    selector_type = Column(String(10), default="css")  # 'css' or 'xpath'
    extraction_type = Column(
        String(20), default="text"
    )  # 'text', 'attribute', or 'html'
    attribute_name = Column(String(50), nullable=True)
    is_required = Column(Boolean, default=False)
    default_value = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationships
    extraction_config = relationship(
        "DbExtractionConfig", back_populates="field_mappings"
    )


# Pydantic models for configuration data


class FieldConfig(BaseModel):
    """
    Pydantic model for field configuration in extraction.
    """

    target_field: str
    selector: str
    extraction_type: str = "text"  # 'text', 'attribute', or 'html'
    attribute_name: Optional[str] = None
    is_required: bool = False
    transformation_rule: Optional[List[Dict[str, Any]]] = None

    model_config = ConfigDict(from_attributes=True)


class GalleryExtractionConfig(BaseModel):
    """
    Pydantic model for gallery extraction configuration.
    """

    correct_urls_paths: List[str]
    schema: Dict[str, Any]
    next_page_selector: Optional[str] = None
    previous_page_selector: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class DetailPageExtractionConfig(BaseModel):
    """
    Pydantic model for detail page extraction configuration.
    """

    fields: List[FieldConfig]

    model_config = ConfigDict(from_attributes=True)


class NavigationConfig(BaseModel):
    """
    Pydantic model for navigation configuration.
    """

    listings_page_url: str

    model_config = ConfigDict(from_attributes=True)


class FilteringConfig(BaseModel):
    """
    Pydantic model for filtering configuration.
    """

    steps: List[Dict[str, Any]]

    model_config = ConfigDict(from_attributes=True)


class LoginConfig(BaseModel):
    """
    Pydantic model for login configuration.
    """

    login_url_path: Optional[str] = None
    username_selector: str
    password_selector: str
    submit_selector: str
    success_check_url_path: str
    expected_url: str
    success_indicator_selector: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class StrategyConfig(BaseModel):
    """
    Pydantic model for strategy configuration.
    """

    navigation_config: NavigationConfig
    filtering_config: Optional[FilteringConfig] = None
    gallery_extraction_config: GalleryExtractionConfig
    detail_page_extraction_config: DetailPageExtractionConfig
    login_config: Optional[LoginConfig] = None

    model_config = ConfigDict(from_attributes=True)


class WebsiteConfig(BaseModel):
    """
    Pydantic model for the complete website configuration.
    """

    website_identifier: str
    website_name: str
    base_url: str
    is_active: bool
    scrape_strategy: str = "multi_step" or "sitemap"
    strategy_config: StrategyConfig
    session_id: str
    accept_cookies: bool

    model_config = ConfigDict(from_attributes=True)


class WebsiteInfo(BaseModel):
    """
    Pydantic model for website information.
    """

    id: int
    name: str
    base_url: str
    is_active: bool
    description: Optional[str] = None
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
WebsiteConfig.model_rebuild()
StrategyConfig.model_rebuild()


__all__ = [
    "DbWebsite",
    "DbLoginConfig",
    "DbNavigationConfig",
    "DbExtractionConfig",
    "DbFieldMapping",
    "WebsiteConfig",
    "WebsiteInfo",
    "LoginConfig",
    "NavigationConfig",
    "ExtractionConfig",
    "FieldMapping",
    "FieldConfig",
    "GalleryExtractionConfig",
    "DetailPageExtractionConfig",
    "FilteringConfig",
    "StrategyConfig",
    "DbWebsiteScrapeConfig",
]
