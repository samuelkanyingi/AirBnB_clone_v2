#!/usr/bin/python3
'''A script that starts a Flask web application
handle srouts /,/hbnb and /c/<text>'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''index page'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def firstpage():
    '''Start page'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def secondpage():
    '''Second Page'''
    return f'C {text}'


if __name__ == '__main__':
    app.run(debug=True)
