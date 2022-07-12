from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

port = 5001
host = '0.0.0.0'

@app.route('/hello')
def hello():
    """Testing..."""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host=host, port=port)
