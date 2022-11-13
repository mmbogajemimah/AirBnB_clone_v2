#!/usr/bin/python3
"""
This script starts a Flask web application
which listens on 0.0.0.0 and port 5000
it has two routes hello_HBNB and HBNB
"""
from flask import Flask
from flask import render_template


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
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    '''
    Displays Python followed by the value of the text variable
    '''
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''
    Displays a number followed by the text " is a number"
    '''
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
