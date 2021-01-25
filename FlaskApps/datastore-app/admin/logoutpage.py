from flask import Blueprint, render_template, current_app, session, Response
import logging
from google.cloud import datastore
client = datastore.Client()
logging.basicConfig(level=logging.DEBUG)
logoutpage = Blueprint("logoutpage", __name__, template_folder="templates")
resp = Response()

"""
    Removes session and logs out the user
"""


@logoutpage.route('/homepage/logout')
def logoutpageview():
    resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
    current_app.logger.info(resp.headers)
    current_app.logger.info('Before popping session cookie: %s', session["user"])
    session.pop("user", None)
    return render_template('logout.html')
