#!/usr/bin/python3

"""
Amenity Class Definition

This module defines the Amenity class, which represents amenities in the
Airbnb-like app
Amenities are additional features or services provided with renatl listings.

Attributes:
    name (str): The name of the amenity

Inherits from:
    BaseMoedel: The base class for all other classes in  the project,
    which provides common attributes abd methods.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Represnents an amenity, including its name. Inherits from BaseModel.

    Attributes:
         name (str): The name of the amenity.

    Examples:
         you can create an Amemity object as follows:
         Amenity = Amenity()
         amenity.name = "Swimming pool"
    """

    name = ""
