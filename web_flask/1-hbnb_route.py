#!/usr/bin/python3
"""Basic Flask App with a second subdomain
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Defines the index domain
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defines the hbnb domain
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
