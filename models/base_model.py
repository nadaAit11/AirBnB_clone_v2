#!/usr/bin/python3
"""
A base class for other classes with common attributes and  methods
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel is a base class for other classes with common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
        - id (str): A unique identifier generated using uuid4.
        - created_at (datetime): The creation date and time.
        - updated_at (datetime): The last update date and time
                                 (initialized to creation time)
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.itmes():
                if key == "created_at" or key == "updated_at":
                    self.__dict[key] = datetime.strptime(value,
                                                         datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Format: "[ClassName] (id) attributes_dict"
        """
        class_name = slef.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with  the current date and time.
        and saves the object to the storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object into a dictionary.

        Returns:
        - dict: A dictionary representation of the object, including
        class name and ISO formatted date and time.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
