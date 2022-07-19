#!/usr/bin/env python3
"""Defines the Skills and Industries tables"""

from api.v1 import db
from datetime import datetime


class Skills(db.Model):
    """Created the table that stores a list of skills"""

    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(60), nullable=False, unique=True)

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        return {
            "name": self.name,
            "id": self.id,
        }

    def __repr__(self) -> str:
        return f"Skill: {self.name}"

