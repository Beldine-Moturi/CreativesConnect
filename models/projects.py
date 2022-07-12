#!/usr/bin/env python3
"""Defines the Project class/Table"""

from api.v1 import db
from datetime import datetime


project_skills = db.Table(
    'project_skills',
    db.Column('project_id', db.String(60), db.ForeignKey('project.id'), primary_key=True),
    db.Column('skill_id', db.String(60), db.ForeignKey('skills.id'), primary_key=True)
    )

project_industry = db.Table(
    'project_industry',
    db.Column('project_id', db.String(60), db.ForeignKey('project.id'), primary_key=True),
    db.Column('industry_id', db.String(60), db.ForeignKey('industry.id'), primary_key=True)
)


class Project(db.Model):
    """Creates the Projects Table"""

    id = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(60), nullable=False)
    description =db.Column(db.String(256))
    cover_photo_url =db.Column(db.String(80))
    organization = db.Column(db.String(80))
    location = db.Column(db.String(60), db.ForeignKey('location.id'))
    skills = db.relationship(
        'Skills',
        secondary=project_skills,
        lazy='joined',
        backref=db.backref('projects', lazy=True)
    )
    industries = db.relationship(
        'Industry',
        secondary=project_industry,
        lazy='joined',
        backref=db.backref('projects', lazy=True)
    )

    def to_dict(self):
        """Returns a dictionary of the objects' attributes"""

        my_dict = self.__dict__.copy()

        if "location" in my_dict:
            location = {
                "city": my_dict.location.city,
                "country": my_dict.location.country
                }
            my_dict["location"] = location

        if "skills" in my_dict:
            skills = [skill.name for skill in my_dict.skills]
            my_dict["skills"] = skills

        if "industries" in my_dict:
            industries = [industry.name for industry in my_dict.insdustries]
            my_dict["industries"] = industries

        my_dict.pop('_sa_instance_state')

        return my_dict
 
    def __repr__(self) -> str:
        return f"Project: {self.title}"
