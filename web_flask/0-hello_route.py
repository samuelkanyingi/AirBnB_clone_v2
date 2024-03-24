#!/usr/bin/python3
'''Script that starts a Flask web application
and displays display "Hello HBNB!"'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''first page'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
