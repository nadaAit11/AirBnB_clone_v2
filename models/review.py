#!/usr/bin/python3
"""defines the Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review

    Attributes:
        place_id (str) : the place id
        user_id (str) : the user id
        text (str) ! the text of the review
    """
