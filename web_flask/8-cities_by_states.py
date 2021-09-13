#!/usr/bin/python3
"""Basic Flask App with a second subdomain
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the database after using it"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    """Shows a dynamic generated html with the list of all
    the states and it's cities"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template("8-cities_by_states.html",
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
