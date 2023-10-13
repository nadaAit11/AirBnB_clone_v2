#!/usr/bin/python3
""" Initialize the BaseModel class with provided attributes or
default values.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
