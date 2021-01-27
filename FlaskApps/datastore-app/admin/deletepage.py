from flask import Blueprint, render_template, current_app, request, redirect, Response
import logging
from helpers import data
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
deletepage = Blueprint("deletepage", __name__, template_folder="templates")
resp = Response()

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
        resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
        current_app.logger.info(resp.headers)
        task = data.Loginbase(request.form["email"])
        task.deleteacc()
        current_app.logger.info('Deleted user account')
        return redirect('/homepage')
    return render_template("delete.html")
