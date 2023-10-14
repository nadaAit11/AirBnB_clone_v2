#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The Place id associated with the  review.
        user_id (str): The User id of the reviewer.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
