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


@app.route('/states', strict_slashes=False)
def states():
    """Shows a dynamic generated html with the list of all the states"""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Shows a dynamic generated html view for a
    specific state.id and it's cities
    if it don't exist, says "Not found"
    """
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template("9-states.html",
                           states=states,
                           cities=cities, id=id)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
