from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DbHouse(Base):
    """
    SQLAlchemy model for house information. This is a unified model that combines
    both DbGalleryHouse and DbDetailHouse, replacing them.
    """

    __tablename__ = "houses"
    __table_args__ = {"schema": "steal_house"}

    id = Column(Integer, primary_key=True)

    # Basic information (from both models)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)

    # Status information (from DbGalleryHouse)
    status = Column(String, nullable=False)
    high_demand = Column(Boolean, default=False)
    demand_message = Column(String, nullable=True)

    # Detailed link (from DbGalleryHouse)
    detail_url = Column(String, nullable=True)

    # Financial information (from DbDetailHouse)
    rental_price = Column(String, nullable=True)
    service_costs = Column(String, nullable=True)

    # Income requirements (from DbDetailHouse)
    min_income_single = Column(String, nullable=True)
    min_income_joint = Column(String, nullable=True)
    read_more_url = Column(String, nullable=True)

    # Features and details (from DbDetailHouse)
    square_meters = Column(Integer, nullable=True)
    bedrooms = Column(Integer, nullable=True)
    energy_label = Column(String, nullable=True)
    available_from = Column(String, nullable=True)
    complex = Column(String, nullable=True)

    # Complex information (from DbDetailHouse)
    complex_name = Column(String, nullable=True)
    complex_description = Column(Text, nullable=True)
    year_of_construction = Column(Integer, nullable=True)
    number_of_objects = Column(String, nullable=True)
    number_of_floors = Column(String, nullable=True)

    # Descriptions (from DbDetailHouse)
    description = Column(Text, nullable=True)

    # Location information (from DbDetailHouse)
    location_map_url = Column(String, nullable=True)

    # Action links (from DbDetailHouse)
    request_viewing_url = Column(String, nullable=True)

    # Extra options (from DbDetailHouse)
    options = Column(Text, nullable=True)

    def has_changes(self, other_db_house):
        """
        Check if this house has differences compared to another house.
        Used to determine if an update is needed.
        """
        # Compare all fields excluding the ID and relationship fields
        for key, value in self.__dict__.items():
            if not key.startswith("_") and key != "id":
                if getattr(other_db_house, key, None) != value:
                    return True
        return False


__all__ = [
    "DbHouse",
    "Base",
]
