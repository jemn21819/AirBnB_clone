#!/usr/bin/python3
""""
Module that contain BaseModel class
"""
import models
import uuid
from datetime import datetime

t = "%Y-%m-%dT%H:%M:%S.%f"
c = "created_at"
u = "updated_at"


class BaseModel:
    """BaseModel class for all other classes"""
    def __init__(self, *args, **kwargs):
        """ initialization the constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, c) and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs[c], t)
                if hasattr(self, u) and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs[u], t)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """string represent BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """update public instance att updated_at to current date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary with all key/value"""
        new_dict = self.__dict__.copy()
        if c in new_dict:
            new_dict[c] = new_dict[c].strftime(t)
        if u in new_dict:
            new_dict[u] = new_dict[u].strftime(t)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
