#!/usr/bin/env python3
"""Defines the creatives class (table)"""

from api.v1 import db
from datetime import datetime


creative_skills = db.Table(
    'creative_skills',
    db.Column('creative_id', db.String(60), db.ForeignKey('creative.id'), primary_key=True),
    db.Column('skill_id', db.String(60), db.ForeignKey('skills.id'), primary_key=True)
    )


class Creative(db.Model):
    """Defines a Creative (Table)"""

    id = db.Column(db.String(60), nullable=False, primary_key= True)
    date_joined = db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    profile_img_url = db.Column(db.String(256))
    cover_photo_url = db.Column(db.String(256))
    about = db.Column(db.String(256), nullable=True)
    location_id = db.Column(db.String(60), db.ForeignKey('location.id'))
    photos = db.relationship('Portfolio', lazy=True, backref=db.backref('creative', lazy='joined'))
    c_skills = db.relationship(
        'Skills',
        secondary=creative_skills,
        lazy='joined',
        backref=db.backref('creatives', lazy=True)
        )

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        my_dict = self.__dict__.copy()

        if "password" in my_dict:
            my_dict.pop("passsword")
        
        if "location" in my_dict:
            location = my_dict.location.name
            my_dict["location"] = location

        if "portfolio" in my_dict:
            portf = {portf.name: portf.image_url for portf in my_dict.portfolio}
            my_dict["portfolio"] = portf

        if "skills" in my_dict:
            skills = [skill.name for skill in my_dict.skills]
            my_dict["skills"] = skills

        my_dict.pop('_sa_instance_state')

        return my_dict

    def __repr__(self) -> str:
        """returns a string representation of objects of this class"""
        return f"Creative: {self.username}"


class Portfolio(db.Model):
    """Creates the table that stores a list of creatives' portfolio urls"""

    id = db.Column(db.String(60), nullable=False, primary_key=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.now())
    image_url = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    creative_id = db.Column(db.String(60), db.ForeignKey('creative.id'), nullable=False)

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        my_dict = self.__dict__.copy()

        if "creative" in my_dict:
            my_dict["creative"] = my_dict.creative.id

        my_dict.pop('_sa_instance_state')

        return my_dict

    def __repr__(self) -> str:
        return f"Portfolio: {self.name}"