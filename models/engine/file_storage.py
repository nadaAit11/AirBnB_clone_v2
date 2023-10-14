#!/usr/bin/python3
"""
Handles the storage and retrieval of objects to/from a JSON file.
"""
import json


class FileStorage:
    """
    This class manages the storage and retrieval of objects tofrom a JSON FILE

    Attributes:
        --file_path (str): Path to the JSON file where objects are stored
        --objects (dict): A dictionary to store objects in memory.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all stored objects.

        Returns:
            dict: A dictionary of objects, wheere keys are in the format
            '<class name>.<object id>'.
        """
        return self.__objects

    def new(self, obj):
        """
        add a new object to the internal dictionary

        Args:
            obj (BaseModel): The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize objetcs to JSON file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict() if hasattr(obj, 'to_dict') else obj
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize objects from JSON file, if the file exits.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    if '.' in key:  # Check if the key contains a period
                        class_name, obj_id = key.split('.')
                        if class_name in globals():
                            if hasattr(globals()[class_name], 'register'):
                                class_obj = globals()[class_name](**obj_data)
                                class_obj.register()
                                self.__objects[key] = class_obj
        except FileNotFoundError:
            pass

    def all_classes(self):
        """
        Returns a dictionary of class names and their associated objects.
        """
        class_dict = {}
        for key, obj in self.__objects.items():
            class_name = key.split('.')[0]
            if class_name not in class_dict:
                class_dict[class_name] = {}
            class_dict[class_name][key] = obj
        return class_dict

    def register(self, class_obj):
        """
        Registers a class with the FileStorage object.

        Args:
            class_obj (class): The class to be registered
        """
        class_name = class_obj.__name__
        if class_name not in self.__objects:
            self.__objects[class_name] = {}
