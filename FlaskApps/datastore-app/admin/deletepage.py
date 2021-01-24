from flask import Blueprint, render_template, current_app, request, redirect
from flask_talisman import Talisman
import logging
from helpers import data
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
deletepage = Blueprint("deletepage", __name__, template_folder="templates")
talisman = Talisman()

"""
    input from form:
    {
        "email": "dipeshdas@gmail.com,
        "password": dipesh97"
    }
    validates its presence in "AUTH kind and removes the user from the kind
"""


@deletepage.route('/homepage/delete', methods=["GET", "POST"])
@talisman(strict_transport_security=True)
def removeacc():
    if request.method == "POST":
        task = data.Loginbase(request.form["email"])
        task.deleteacc()
        current_app.logger.info('Deleted user account')
        return redirect('/homepage')
    return render_template("delete.html")
