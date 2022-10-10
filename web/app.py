from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from api.v1 import db
from models.skills import *
from models.locations import *
from models.creatives import *
from models.projects import *

app = Flask(__name__)
app.url_map.strict_slashes = False

port = 5001
host = '0.0.0.0'

# The navigation bar
main = Navbar('',\
    View('Home', 'index'),
    View('Creatives', 'creatives'),
    View('Projects', 'projects'),
    View('Contact us', 'contact')
    )

nav = Nav(app)
nav.register_element('main_nav', main)

# get list of all locations and skills --> to apply filters in
# creatives and projects pages
locations = db.session.execute(db.select(Location).order_by(Location.name)).scalars()
skills = db.session.execute(db.select(Skills).order_by(Skills.name)).scalars()

# Routes
@app.route('/')
def index():
    """The landing page"""

    return render_template("index.html")

@app.route('/creatives')
def creatives():
    """The creatives search page"""

    return render_template("creatives.html", skills=skills, locations=locations)

@app.route('/projects')
def projects():
    """The projects search page"""

    return render_template("projects.html", skills=skills, locations=locations)

@app.route('/contact')
def contact():
    """The contact page"""

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
