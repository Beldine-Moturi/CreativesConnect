#!/usr/bin/env python3
"""Starts our Flask application"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PWD = getenv('MYSQL_PWD')
MYSQL_HOST = getenv('MYSQL_HOST')
MYSQL_DB = getenv('MYSQL_DB')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(
    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.route('hello')
def hello():
    """Testing..."""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host=host, port=port)
