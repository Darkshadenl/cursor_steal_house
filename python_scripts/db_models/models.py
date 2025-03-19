from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GalleryHouse(Base):
    """SQLAlchemy model for basic house information in gallery view"""
    __tablename__ = "gallery_houses"
    __table_args__ = {"schema": "steal_house"}
    
    id = Column(Integer, primary_key=True)
    
    # Address and location
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    # Status
    status = Column(String, nullable=False)
    
    # Media
    image_url = Column(String, nullable=True)
    
    # Metadata
    high_demand = Column(Boolean, default=False)
    demand_message = Column(String, nullable=True)
    
    # Link
    detail_url = Column(String, nullable=True)
    
    # Relationship
    detail_house = relationship("DetailHouse", back_populates="gallery_reference", uselist=False)


class DetailHouse(Base):
    """SQLAlchemy model for detailed house information"""
    __tablename__ = "detail_houses"
    __table_args__ = {"schema": "steal_house"}
    
    id = Column(Integer, primary_key=True)
    
    # Foreign key to gallery house
    gallery_id = Column(Integer, ForeignKey("steal_house.gallery_houses.id"), nullable=True)
    gallery_reference = relationship("GalleryHouse", back_populates="detail_house")
    
    # Basic information
    address = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=True)
    
    # Financial information
    rental_price = Column(String, nullable=False)
    service_costs = Column(String, nullable=True)
    
    # Income requirements
    min_income_single = Column(String, nullable=True)
    min_income_joint = Column(String, nullable=True)
    read_more_url = Column(String, nullable=True)
    
    # Features and details
    square_meters = Column(Integer, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    energy_label = Column(String, nullable=True)
    status = Column(String, nullable=False)
    available_from = Column(String, nullable=True)
    complex = Column(String, nullable=True)
    
    # Complex information
    complex_name = Column(String, nullable=True)
    complex_description = Column(Text, nullable=True)
    year_of_construction = Column(Integer, nullable=True)
    number_of_objects = Column(String, nullable=True)
    number_of_floors = Column(String, nullable=True)
    complex_image_url = Column(String, nullable=True)
    
    # Descriptions
    description = Column(Text, nullable=False)
    
    # Location information
    location_map_url = Column(String, nullable=True)
    
    # Extra options
    options = Column(Text, nullable=True)
    
    # Floor plans are stored in a related table
    floor_plans = relationship("FloorPlan", back_populates="house")


class FloorPlan(Base):
    """SQLAlchemy model for floor plans"""
    __tablename__ = "floor_plans"
    __table_args__ = {"schema": "steal_house"}
    
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey("steal_house.detail_houses.id"), nullable=False)
    image_url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    house = relationship("DetailHouse", back_populates="floor_plans") 