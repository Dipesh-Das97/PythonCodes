from flask import Blueprint, render_template, current_app, request, redirect, Response
import logging
from helpers import data
logging.basicConfig(level=logging.DEBUG)
forgotpasswordpage = Blueprint("forgotpasswordpage", __name__, template_folder="templates")
resp = Response()

"""
    This page lets a user change the password of a user if password forgotten.
    Validates user "email" from the form 
    and updates "password" in kind "AUTH" with request.form["passord"]
"""


@forgotpasswordpage.route('/homepage/forgotpassword', methods=["GET", "POST"])
def forgotpassview():
    if request.method == "POST":
        resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
        current_app.logger.info(resp.headers)
        task = data.ForgotPassword(request.form["email"], request.form["password"])
        entity = task.forgotpassword()
        current_app.logger.info('After creating new password %s', entity)
        return redirect('/homepage/login')
    return render_template("forgotpassword.html")
