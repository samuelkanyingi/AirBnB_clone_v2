#!/usr/bin/python3
'''A  script that starts a Flask web application
and uses routes / and /hbnb'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    '''Index page'''
    return "Hello HBNB!"


@app.route('/hbnb')
def firstpage():
    '''start page'''
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
