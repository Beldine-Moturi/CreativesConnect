#!/usr/bin/env python3
"""Runs the flask app that hosts APIs"""
#from api.v1 import app
#from flask import make_response, jsonify
# from api.v1.views import app_views
# from flask_cors import CORS

"""
port = 5000
host = '0.0.0.0'
"""
# register blueprints
# app.register_blueprint(app_views)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# cross-origin resource sharing
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

"""
@app.errorhandler(404)
def page_not_found(error):
    renders a custom error message for non-existent resources
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    Runs the flask app
    app.run(host=host, port=port, debug=True, threaded=True)
"""