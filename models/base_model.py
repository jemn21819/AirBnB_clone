#!/usr/bin/python3
""""
Module that contain BaseModel class
"""
import models
import uuid
from datetime import datetime

date_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class for all other classes"""
    def __init__(self, *args, **kwargs):
        """ initialization the constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_time)
                if '__class__' != key:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string represent BaseModel class"""
        return "[{:s}] ({}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__)

    def save(self):
        """update public instance att updated_at to current date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary with all key/value"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(date_time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(date_time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
