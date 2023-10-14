#!/usr/bin/python3
""" Defines the Place class """
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place

    Attributes:
        city_id (str): the city id
        user_id (str) : the user id
        name (str) : the name of the place
        description (str) : the description of the place
        number_rooms (int) : the number of rooms in the place
        number_bathrooms (int) : the number of bathrooms in the place
        max_guest (int) : the maximum number of guests of the place
        price_by_night (int) : the price by night of the place
        latitude (float) : the latitude of the place
        longitude (float) : the longitude of the place
        amenity_ids (list) : a list of amenity ids
    """
