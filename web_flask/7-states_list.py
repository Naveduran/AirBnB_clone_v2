#!/usr/bin/python3
"""Basic Flask App with a second subdomain
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    dic = storage.all(States)
    return render_template("states_list.html", dic)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
