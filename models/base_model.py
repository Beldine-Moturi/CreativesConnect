#!/usr/bin/env python3
"""Defines the Base Model class that all other
classes in this project will inherit from"""
from datetime import datetime
import models
import uuid
from app.app import db


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The Base class for all objects of this project
    All other classes will inherit from this class"""

    id = db.Column(db.String(60), nullable=False, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes instances of this class"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self) -> str:
        """String representation of the Base Model class"""

        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
            )

    def save(self):
        """updates the attribute updated_at with the current datetime
        saves the updated object to the storage"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys and values of the instance"""

        dictionary = self.__dict__.copy()

        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(time)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(time)
        dictionary["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""

        models.storage.delete(self)

    
