#!/usr/bin/python3
"""
Flask module that returns a route at /
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A route that displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ A route that displays C and input text """
    return "C %s" % escape(text.replace("_", " "))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
