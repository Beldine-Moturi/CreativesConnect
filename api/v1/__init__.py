#!/usr/bin/env python3
"""Instantiates and configures a flask app for the APIs"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from views import app_views
from flask_cors import CORS
from flask import make_response, jsonify



MYSQL_USER = 'root' #getenv('MYSQL_USER')
MYSQL_PWD = 'root' #getenv('MYSQL_PWD')
MYSQL_HOST = 'localhost' #getenv('MYSQL_HOST')
MYSQL_DB = 'CreativesConnect' #getenv('MYSQL_DB')

port = 5000
host = '0.0.0.0'

app = Flask(__name__)

# app configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}?charset=utf8mb4'.format(
    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False

# register blueprints and cors
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# MySQL database
db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(error):
    """renders a custom error message for non-existent resources"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """Runs the flask app"""
    app.run(host=host, port=port, debug=True, threaded=True)
