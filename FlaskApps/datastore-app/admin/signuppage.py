from flask import Blueprint, render_template, current_app, request, redirect, Response
from flask_bcrypt import Bcrypt
import logging
from helpers import data
logging.basicConfig(level=logging.DEBUG)
signuppage = Blueprint("signuppage", __name__, template_folder="templates")
bcrypt = Bcrypt()
resp = Response()


"""
    This page signs up a user to our app by adding the form inputs to datastore.
    Form input:
    {
        'name': 'Dipesh Das', 
        'email': 'dipeshdas@gmail.com', 
        'password': 'dipesh97'
    }
    
"""


@signuppage.route('/homepage/signup', methods=["GET", "POST"])
def signuppageview():
    if request.method == "POST":
        resp.headers['Content-Type'] = ' application/x-www-form-urlencoded'
        current_app.logger.info(resp.headers)
        entity = data.Signupbase(request.form["email"], request.form["name"], request.form["password"])
        task = entity.signupinfo()
        current_app.logger.info('Created user details: %s', task)
        return redirect('/homepage/login')
    return render_template('signup.html')
