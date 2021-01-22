from flask import Blueprint, render_template, current_app, session
from flask_talisman import Talisman
import logging
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
logoutpage = Blueprint("logoutpage", __name__, template_folder="templates")
talisman = Talisman()

"""
    Removes session and logs out the user
"""


@logoutpage.route('/homepage/logout')
@talisman(strict_transport_security=True)
def logoutpageview():
    current_app.logger.info('Before popping session cookie: %s', session["user"])
    session.pop("user", None)
    return render_template('logout.html')
