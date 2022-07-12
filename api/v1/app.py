from api.v1 import app

port = 5000
host = '0.0.0.0'


if __name__ == "__main__":
    app.run(host=host, port=port)