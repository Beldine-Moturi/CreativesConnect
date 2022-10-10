#!/usr/bin/env python3
"""Defines the Project class/Table"""

from api.v1 import db
from datetime import datetime


project_skills = db.Table(
    'project_skills',
    db.Column('project_id', db.String(60), db.ForeignKey('project.id'), primary_key=True),
    db.Column('skill_id', db.String(60), db.ForeignKey('skills.id'), primary_key=True)
    )


class Project(db.Model):
    """Creates the Projects Table"""

    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(60), nullable=False, unique=True)
    description =db.Column(db.Text)
    cover_photo_url =db.Column(db.String(80))
    organization = db.Column(db.String(80))
    location_id = db.Column(db.String(60), db.ForeignKey('location.id'))
    p_skills = db.relationship(
        'Skills',
        secondary=project_skills,
        lazy='joined',
        backref=db.backref('projects', lazy=True)
    )

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        my_dict = self.__dict__.copy()

        if "location_id" in my_dict:
            location = self.location
            my_dict["location"] = location
            my_dict.pop('location_id')

        if "p_skills" in my_dict:
            skills = [skill.name for skill in my_dict['p_skills']]
            my_dict["skills"] = skills
            my_dict.pop('p_skills')

        my_dict.pop('_sa_instance_state')

        return my_dict
 
    def __repr__(self) -> str:
        return f"Project: {self.title}"
