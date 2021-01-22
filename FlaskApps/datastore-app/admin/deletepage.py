from flask import Blueprint, render_template, current_app, request, redirect
import logging
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
deletepage = Blueprint("deletepage", __name__, template_folder="templates")

"""
    input from form:
    {
        "email": "dipeshdas@gmail.com,
        "password": dipesh97"
    }
    validates its presence in "AUTH kind and removes the user from the kind
"""


@deletepage.route('/homepage/delete', methods=["GET", "POST"])
def removeacc():
    if request.method == "POST":
        key = client.key("AUTH", request.form["email"])
        client.delete(key)
        current_app.logger.info('Deleted user account')
        return redirect('/homepage')
    return render_template("delete.html")