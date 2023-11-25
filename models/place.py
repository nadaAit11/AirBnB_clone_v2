#!/usr/bin/python3
"""
Defines the Place class.
"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    Represent a place.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Places.
        city_id (Column): The city id of the Place.
        user_id (Column): The user id of the Place.
        name (Column): The name of the Place.
        description (Column): The description of the Place.
        number_rooms (Column): The number of rooms in the Place.
        number_bathrooms (Column): The number of bathrooms in the Place.
        max_guest (Column): The maximum number of guests of the Place.
        price_by_night (Column): The price by night of the Place.
        latitude (Column): The latitude of the Place.
        longitude (Column): The longitude of the Place.
        amenity_ids (list): A list of Amenity ids.
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []