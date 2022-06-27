#!/usr/bin/env python3
"""Defines the class DBStorage"""
from app.app import app, db
from os import getenv

classes = []


class DBStorage():
    """Defines functions that interact with the MYSQL database"""

    def __init__(self):
        """Instantiates objects of this class"""
        if getenv('MYSQL_ENV') == 'test':
            db.drop_all()

    def all(self, cls=None):
        """Returns all objects/ objects of a
        certain class currently in storage"""

        all_objs = {}
        if cls:
            objs = cls.query.all()
            for obj in objs:
                all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for c in classes:
                c = eval(c)
                objs = c.query.all()
                for obj in objs:
                    all_objs[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return (all_objs)

    def new(self, obj=None):
        """Adds the object(obj) to the database storage"""

        if obj:
            db.session.add(obj)

    def save(self):
        """Commits all changes made to the database"""

        db.session.commit()

    def delete(self, obj=None):
        """deletes the object (obj) from the database"""

        if obj:
            db.session.delete(obj)

    def reload(self):
        """creates database tables """

        db.create_all()

    def get(self, cls, id):
        """Retrieves one object:
            - cls: the object's class
            - id: string representing the object ID
            - Returns the object based on the class and its ID
            or None if not found
        """

        if (cls and id) and cls in classes:
            obj = "{}.{}".format(cls, id)
            all_objs = self.all(cls)
            return all_objs.get(obj)
        return None

    def count(self, cls=None):
        """Counts the number of objects in storage:
            - cls: the objects' class
            - Returns the number of oobjects of class cls or all
              classes if cls is None
        """

        count = len(self.all(cls))
        return count