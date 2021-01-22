from flask import Blueprint, render_template, current_app, request, redirect
import logging
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
forgotpasswordpage = Blueprint("forgotpasswordpage", __name__, template_folder="templates")


"""
    This page lets a user change the password of a user if password forgotten.
    Validates user "email" from the form 
    and updates "password" in kind "AUTH" with request.form["passord"]
"""


@forgotpasswordpage.route('/homepage/forgotpassword', methods=["GET", "POST"])
def forgotpassview():
    if request.method == "POST":
        with client.transaction():
            key = client.key("AUTH", request.form["email"])
            entity = client.get(key)
            current_app.logger.info('Before creating new password %s', entity)
            if not entity.get("email") == request.form["email"] and request.form["password"]:
                return "Wrong Email or enter new password again"
            entity["password"] = request.form["password"]
            client.put(entity)
            current_app.logger.info('After creating new password %s', entity)
        return redirect('/homepage/login')
    return render_template("forgotpassword.html")
