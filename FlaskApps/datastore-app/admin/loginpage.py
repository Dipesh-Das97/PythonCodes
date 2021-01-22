from flask import Blueprint, render_template, current_app, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
import logging
from google.cloud import datastore
import datetime
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
loginpage = Blueprint("loginpage", __name__, template_folder="templates")
bcrypt = Bcrypt()

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


@loginpage.route('/homepage/login', methods=["GET", "POST"])
def loginpageview():
    if request.method == "POST":
        key = client.key("AUTH", request.form["email"])
        entity = client.get(key)
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
def postlog():
    if "user" in session:
        current_app.logger.info('Available session cookies: %s', session["user"])
        return render_template("postlogin.html")
    return redirect('/homepage/login')
