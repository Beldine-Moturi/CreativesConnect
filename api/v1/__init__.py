#!/usr/bin/env python3
"""Starts our Flask application"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

MYSQL_USER = 'root' #getenv('MYSQL_USER')
MYSQL_PWD = 'root' #getenv('MYSQL_PWD')
MYSQL_HOST = 'localhost' #getenv('MYSQL_HOST')
MYSQL_DB = 'CreativesConnect' #getenv('MYSQL_DB')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(
    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)

