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


@app.route('/states_list', strict_slashes=False)
def states():
    
    """Shows a dynamic generated html with the list of all the states"""
    dic = storage.all(State).values()
    listt = sorted(states, key=lambda k: k.name)
    return render_template("states_list.html", list=listt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
