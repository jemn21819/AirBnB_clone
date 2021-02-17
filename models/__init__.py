#!/usr/bin/python3
"""
initialize the models package
"""

from models.engine.file_storage import FileStorage


classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

storage = FileStorage()
storage.reload()
