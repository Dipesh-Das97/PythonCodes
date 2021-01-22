from flask import Blueprint, render_template, current_app, request, redirect
from flask_bcrypt import Bcrypt
import logging
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
signuppage = Blueprint("signuppage", __name__, template_folder="templates")
bcrypt = Bcrypt()


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
        with client.transaction():
            current_app.logger.info('Form Details: %s', request.form)
            key = client.key("AUTH", request.form["email"])
            task = datastore.Entity(key=key)
            task.update(
                {
                    "name": request.form["name"],
                    "email": request.form["email"],
                    "password": bcrypt.generate_password_hash(request.form["password"])
                }
            )
            client.put(task)
            current_app.logger.info('Created user details: %s', task)
        return redirect('/homepage/login')
    return render_template('signup.html')
