#!/usr/bin/python3
"""
This script starts a Flask web application
that lisens on host 0.0.0.0 and port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """The index page displays a hello HBNB message"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
