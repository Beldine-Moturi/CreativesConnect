#!/usr/bin/env python3
"""Defines views for the creatives page"""
from views import app_views
from flask import jsonify, request, make_response, url_for, abort
# from api.v1 import app
from models.creatives import *
from models.skills import *
from models.locations import *
from models.projects import *
import uuid
from api.v1 import db

"""
def make_uri(obj):
    creates a uri from obj's id attribute

    new_obj = {}
    for field in obj:
        if field == "id":
            new_obj['uri'] = url_for(".get_creatives", c_id=obj['id'], _external=True)
        else:
            new_obj[field] = obj[field]

    return new_obj
"""

@app_views.route('/creatives', methods=['GET'])
def get_creatives():
    """Returns a list of all creatives in the database"""

    creatives = []
    c = db.session.execute(db.select(Creative).order_by(Creative.id)).unique().scalars()
    for creative in c:
        creatives.append(creative.to_dict())
    return jsonify(creatives)

@app_views.route('/creatives/<c_id>', methods=['GET'])
def get_creative(c_id):
    """Returns information about a specific creative"""

    creative = db.session.execute(db.select(Creative).filter_by(id=c_id)).one()
    if creative is None:
        return make_response(jsonify({'error': 'Not Found'}), 404)

    c = creative.to_dict()
    return jsonify(c)

@app_views.route('/creatives', methods=['POST'])
def create_creative():
    """Creates a new creative"""

    req = request.get_json()
    if not req:
        return make_response(jsonify({'error': 'Data is not a valid json'}), 400)
    if 'username' not in req:
        return make_response(jsonify({'error': 'missing username'}))
    if 'password' not in req:
        return make_response(jsonify({'error': 'missing password'}))
    
    creative = Creative(**req)
    creative.id = str(uuid.uuid4())
    db.session.add(creative)
    db.session.commit()
    return make_response(jsonify(creative.to_dict()), 201)

@app_views.route('/creatives/<c_id>', methods=['DELETE'])
def delete_creative(c_id):
    """Deletes a creative from the database"""

    creative = db.session.execute(db.select(Creative).filter_by(id=c_id)).one()
    if not creative:
        return make_response(jsonify({'error': 'Not Found'}), 404)
    db.session.delete(creative)
    db.session.commit()

@app_views.route('/creatives/<c_id>', methods=['PUT'])
def update_creative(c_id):
    """Updates information about a creative"""

    creative = db.session.execute(db.select(Creative).filter_by(id=c_id)).one()
    if creative is None:
        return make_response(jsonify({'error': 'Not Found'}), 404)

    req = request.get_json()
    if not req:
        return make_response(jsonify({'error': 'Data is not a valid json'}))

    for attr, val in req.items():
        if attr not in ['date_joined', 'id']:
            setattr(creative, attr, val)

    db.session.commit()
    return make_response(jsonify(creative.to_dict()))
