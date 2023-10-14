#!/usr/bin/python3
"""
A base class for other classes with common attributes and  methods
"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from .engine import file_storage


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
        if kwargs:  # If kwargs is not empty, initialize from dict
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert strings to datetime objects
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == 'first_name':
                    setattr(self, key, value)
        else:  # Otherwise, create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.first_name = ""

    def __str__(self):
        """
        Returns a string representation of the object.

        Format: "[ClassName] (id) attributes_dict"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with  the current date and time.
        and saves the object to the storage
        """
        self.updated_at = datetime.now()
        FileStorage().register(BaseModel)
        FileStorage().new(self)
        FileStorage().save()

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

    def register(self):
        """Register the BaseModel class with the storage system."""
        from models import storage
        storage.register(BaseModel)
