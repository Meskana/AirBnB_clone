#!/usr/bin/python3
"""
a class BaseModel that defines all common attributes/methods
for other classes
"""

import uuid
import json
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        initailze the BaseModel class

        Args:
            args: variable positional argument
            kwargs: variable keyword argument
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        time_obj = datetime.strptime(
                            value,
                            "%Y-%m-%dT%H:%M:%S.%f"
                        )
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dateyime.now()

    def __str__(self):
        """Return formadet string"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            return a dictionary containing all keys/values
            of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
