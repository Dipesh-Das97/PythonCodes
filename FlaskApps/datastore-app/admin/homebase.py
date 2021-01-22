from flask import Blueprint, render_template, current_app
from flask_talisman import Talisman
import logging
logging.basicConfig(level=logging.DEBUG)
homebase = Blueprint("homebase", __name__, template_folder="templates")
talisman = Talisman()


@homebase.route('/')
@talisman(strict_transport_security=True)
def home():
    current_app.logger.info('Starting point of app')
    return render_template('home.html')


@homebase.route('/homepage')
@talisman(strict_transport_security=True)
def homepage():
    current_app.logger.info('Homepage of app')
    return render_template('homepage.html')
