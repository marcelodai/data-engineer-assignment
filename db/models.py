from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ParkData(Base):
    __tablename__ = 'park_data'
    
    park_id = Column(Integer, primary_key=True)
    area_name = Column(String)
    area_id = Column(String)
    park_name = Column(String)
    date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    total_time_minutes = Column(Integer)
    park_conditions = Column(Text)
    litter = Column(Text)
    temperature_weather = Column(String)
    
    squirrels = relationship('SquirrelData', back_populates='park')

class SquirrelData(Base):
    __tablename__ = 'squirrel_data'
    
    squirrel_id = Column(String, primary_key=True)
    park_id = Column(Integer, ForeignKey('park_data.park_id'))
    primary_fur_color = Column(String)
    highlights_in_fur_color = Column(String)
    color_notes = Column(Text)
    location = Column(String)
    above_ground_height_feet = Column(Integer)
    specific_location = Column(Text)
    activities = Column(Text)
    interactions_with_humans = Column(Text)
    other_notes = Column(Text)
    squirrel_latitude = Column(Float)
    squirrel_longitude = Column(Float)
    
    park = relationship('ParkData', back_populates='squirrels')

class OtherAnimalSightings(Base):
    __tablename__ = 'other_animal_sightings'
    
    id = Column(Integer, primary_key=True)
    park_id = Column(Integer, ForeignKey('park_data.park_id'))
    animal = Column(String)

class Activities(Base):
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True)
    squirrel_id = Column(String, ForeignKey('squirrel_data.squirrel_id'))
    activity = Column(String)