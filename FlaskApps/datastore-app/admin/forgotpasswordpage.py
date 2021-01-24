from flask import Blueprint, render_template, current_app, request, redirect
from flask_talisman import Talisman
import logging
from helpers import data
logging.basicConfig(level=logging.DEBUG)
forgotpasswordpage = Blueprint("forgotpasswordpage", __name__, template_folder="templates")
talisman = Talisman()

"""
    This page lets a user change the password of a user if password forgotten.
    Validates user "email" from the form 
    and updates "password" in kind "AUTH" with request.form["passord"]
"""


@forgotpasswordpage.route('/homepage/forgotpassword', methods=["GET", "POST"])
@talisman(strict_transport_security=True)
def forgotpassview():
    if request.method == "POST":
        task = data.ForgotPassword(request.form["email"], request.form["password"])
        entity = task.forgotpassword()
        current_app.logger.info('After creating new password %s', entity)
        return redirect('/homepage/login')
    return render_template("forgotpassword.html")
