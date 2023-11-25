#!/usr/bin/python3
"""
This module defines the City class, which represents a city in the
HBNB project.
It inherits from the BaseModel and Base classes and provides attributes
for city name and state ID.
"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """
    City Class

    Represents a city in the HBNB project.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (Column): The name of the City, represented as a string
        of up to 128 characters. It cannot be null.
        state_id (Column): The state id of the City, represented
        as a string of up to 60 characters. It cannot be null and
        is a foreign key to states.id.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)