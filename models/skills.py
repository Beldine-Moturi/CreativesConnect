#!/usr/bin/env python3
"""Defines the Skills and Industries tables"""

from api.v1 import db
from datetime import datetime


class Skills(db.Model):
    """Created the table that stores a list of skills"""

    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    updated_at = db.Column(db.Date, default=datetime.utcnow)
    name = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        return {
            "name": self.name,
            "id": self.id,
        }

    def __repr__(self) -> str:
        return f"Skill: {self.name}"


class Industry(db.Model):
    """Creates the table that stores a list of Industry categories"""

    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    updated_at = db.Column(db.Date, default=datetime.utcnow)
    name = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        """Returns a dictionary of the object's attributes"""

        return {
            "name": self.name,
            "id": self.id
        }

    def __repr__(self) -> str:
        return f"Industry: {self.name}"