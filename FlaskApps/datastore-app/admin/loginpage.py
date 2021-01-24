from flask import Blueprint, render_template, current_app, request, redirect, url_for, session
from functools import wraps
from flask_bcrypt import Bcrypt
from flask_talisman import Talisman
from helpers import data
import logging
import datetime
logging.basicConfig(level=logging.DEBUG)
loginpage = Blueprint("loginpage", __name__, template_folder="templates")
bcrypt = Bcrypt()
talisman = Talisman()
"""
    loginpageview() handles the login: For eg: Input in form is: 
    {
        "email": "dipeshdas@gmail.com
        "password": "dipesh97"
    }
    and checks if and entity in kind "AUTH" is present with the ID as request.form["email"].
    While at it creates a session cookie for the user 
    and the redirects to post login page for correct authentication else redirects to the signup page.
    
    postlog() handles checking for a session cookie generated and redirects users to the login page 
    if not logged in
"""

"""
class Database:
    def __init__(self, email):
        self.email = email

    def logininfo(self):
        key = client.key("AUTH", self.email)
        entity = client.get(key)
        return entity
"""


def login_required(f):
    @wraps(f)
    def decorated_function():
        if session["user"] is None:
            return redirect('/homepage/login')
        return render_template("postlogin.html")
    return decorated_function


@loginpage.route('/homepage/login', methods=["GET", "POST"])
@talisman(strict_transport_security=True)
def loginpageview():
    if request.method == "POST":
        task = data.Loginbase(request.form["email"])
        entity = task.logininfo()
        current_app.logger.info('Details fetched: %s', entity)
        current_app.logger.info('Form Details: %s', request.form)
        correctpassword = bcrypt.check_password_hash(entity.get("password"), request.form["password"])
        usercred = entity.get("email") == request.form["email"] and correctpassword
        if usercred:
            session["user"] = bcrypt.generate_password_hash(request.form["email"] + str(datetime.datetime.now()))
            current_app.logger.info('Session stored from user: %s', session["user"])
            return redirect(url_for("loginpage.postlog"))
        else:
            return redirect("/homepage/signup")
    return render_template("login.html")


@loginpage.route('/homepage/postlogin')
@talisman(strict_transport_security=True)
@login_required
def postlog():
    pass
