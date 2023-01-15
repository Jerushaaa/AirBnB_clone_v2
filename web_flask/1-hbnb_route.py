#!/usr/bin/python3
""" Starts a Flash Web Application HBNB"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=Fase)
def hbnb_route():
    """prints Hello HBNB"""l
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
