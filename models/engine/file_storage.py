#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None:
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects
        if cls in classes.values():
            cpy = {}
            for k, v in FileStorage.__objects.items():
                if isinstance(v, cls):
                    cpy[k] = FileStorage.__objects[k]
            return cpy

    def new(self, obj):
        """
        Add the given object to the object storage.

        This method adds the given object to the object storage dictionary.

        Args:
           obj: The object to be added to the storage

        Returns:
           None
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serialize the  object storage to a JSON file.

        This method serializes the '__objects' dictionary, containing objects,
        the the JSON file specified by '__file_path'.

        Returns:
            None
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
    def delete(self, obj=None):
        """delete object, if specified"""
        if not obj:
            return
        if obj.__class__.__name__+"."+obj.id in FileStorage.__objects:
            del FileStorage.__objects[obj.__class__.__name__+"."+obj.id]
        self.save()
