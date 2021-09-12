#!/usr/bin/python3
"""Basic Flask App with a second subdomain
"""

from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ Defines the text domain
    """
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Defines the python domain
    """
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


@app.route('/python', strict_slashes=False)
def python2():
    """ Defines the python domain
    """
    text = "is cool"
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Defines the number domain
    """
    if type(n) == int:
        return "{} is a number".format(escape(n))
    return ""


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """ Defines a template for a number
    """
    if type(n) == int:
        return render_template('5-number.html', n=n)
    return ""


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Defines the template for a even or odd numbers
    """
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=5000)
