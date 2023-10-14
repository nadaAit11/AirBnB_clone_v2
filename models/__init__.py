#!/usr/bin/python3
""" Initialize the BaseModel class with provided attributes or
default values.
"""


from models.engine.file_storage import FileStorage


# Create a FileStorage instance and reload data from the storage file.
storage = FileStorage()
storage.reload()
