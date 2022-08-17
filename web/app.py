from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View


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

# Routes
@app.route('/')
def index():
    """The landing page"""

    return render_template("index.html")

@app.route('/creatives')
def creatives():
    """The creatives search page"""

    return render_template("creatives.html")

@app.route('/projects')
def projects():
    """The projects search page"""

    return render_template("projects.html")

@app.route('/contact')
def contact():
    """The contact page"""

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
