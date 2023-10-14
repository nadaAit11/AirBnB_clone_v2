#!/usr/bin/python3

"""
City Class Definition

This module defines the city class, which represents a city in the HBNB project
It inherits from the BaseModel class and provides attributes for state ID
and City name.

Attributes:
    state_id (str): The state ID to which the city belongs.
    name (str): The name of the city

Inherits from:
    BaseModel

Usage:
    You  can create a city object as follows:

    city = City()

    You can access its attributes like state_id and name.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class

    Represents a city in the HBNB project.

    Attributes:
        state_id (str): The state ID to which the city belongs.
        name (str): The name of the city
    """

    state_id = ""
    name = ""
