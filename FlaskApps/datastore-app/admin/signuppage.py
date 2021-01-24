from flask import Blueprint, render_template, current_app, request, redirect
from flask_bcrypt import Bcrypt
from flask_talisman import Talisman
import logging
from helpers import data
logging.basicConfig(level=logging.DEBUG)
signuppage = Blueprint("signuppage", __name__, template_folder="templates")
bcrypt = Bcrypt()
talisman = Talisman()


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
@talisman(strict_transport_security=True)
def signuppageview():
    if request.method == "POST":
        entity = data.Signupbase(request.form["email"], request.form["name"], request.form["password"])
        task = entity.signupinfo()
        current_app.logger.info('Created user details: %s', task)
        return redirect('/homepage/login')
    return render_template('signup.html')
