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


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    '''
    Displays C followed by the value of text variable
    '''
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
