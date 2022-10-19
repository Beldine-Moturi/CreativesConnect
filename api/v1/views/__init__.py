#!/usr/bin/env python3
"""Initializes Blueprint views"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from views.creatives import *
from views.projects import *
