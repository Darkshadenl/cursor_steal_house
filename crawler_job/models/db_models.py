from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Text,
    JSON,
    DateTime,
    func,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DbHouse(Base):
    """
    SQLAlchemy model for house information with a unified schema to store all property data.
    """

    __tablename__ = "houses"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)

    # Basic information
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)

    # Status information
    status = Column(String, nullable=False)
    high_demand = Column(Boolean, default=False)
    demand_message = Column(String, nullable=True)

    # Detailed link
    detail_url = Column(String, nullable=True)

    # Financial information
    rental_price = Column(String, nullable=True)
    service_costs = Column(String, nullable=True)

    # Income requirements
    min_income_single = Column(String, nullable=True)
    min_income_joint = Column(String, nullable=True)
    read_more_url = Column(String, nullable=True)

    # Features and details
    square_meters = Column(Integer, nullable=True)
    bedrooms = Column(Integer, nullable=True)
    energy_label = Column(String, nullable=True)
    available_from = Column(String, nullable=True)
    complex = Column(String, nullable=True)

    # Complex information
    complex_name = Column(String, nullable=True)
    complex_description = Column(Text, nullable=True)
    year_of_construction = Column(Integer, nullable=True)
    number_of_objects = Column(String, nullable=True)
    number_of_floors = Column(String, nullable=True)

    # Description
    description = Column(Text, nullable=True)

    # Location information
    location_map_url = Column(String, nullable=True)

    # Action links
    request_viewing_url = Column(String, nullable=True)

    # Extra options
    options = Column(Text, nullable=True)

    def has_changes(self, other):
        """
        Check if another DbHouse instance has different values.
        Used to determine if an update is necessary.

        Args:
            other: Another DbHouse instance to compare with

        Returns:
            bool: True if there are differences, False otherwise
        """
        # Check all columns except id (primary key)
        for column in self.__table__.columns:
            if column.name == "id":
                continue

            self_value = getattr(self, column.name)
            other_value = getattr(other, column.name, None)

            if self_value != other_value:
                return True

        return False


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


__all__ = [
    "DbHouse",
    "DbWebsiteScrapeConfig",
    "Base",
]
