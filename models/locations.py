#!/usr/bin/env python3
"""Defines the table that stores all Locations data"""

from api.v1 import db


class Location(db.Model):
    """Creates the Location table"""

    id = db.Column(db.String(60), nullable=False, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    creatives = db.relationship('Creative', lazy=True, backref=db.backref('location', lazy='joined'))
    projects = db.relationship('Project', lazy=True, backref=db.backref('location', lazy='joined'))

    def to_dict(self):
        """Returns a dictionary of the object's attributes"""

        return {
            "id": self.id,
            "name": self.name,
            "creatives": [c.id for c in self.creatives],
            "projects": [p.id for p in self.projects]
        }

    def __repr__(self):
        """returns a string representation of the object"""

        return f"Location: {self.name}"