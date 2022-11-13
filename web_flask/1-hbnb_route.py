#!/usr/bin/python3
"""
This script starts a Flask web application
which listens on 0.0.0.0 and port 5000
it has two routes hello_HBNB and HBNB
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """
    This route displays Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    This page displays HBNB
    '''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
