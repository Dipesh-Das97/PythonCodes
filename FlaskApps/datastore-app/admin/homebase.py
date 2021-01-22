from flask import Blueprint, render_template, current_app
import logging
logging.basicConfig(level=logging.DEBUG)
homebase = Blueprint("homebase", __name__, template_folder="templates")


@homebase.route('/')
def home():
    current_app.logger.info('Starting point of app')
    return render_template('home.html')


@homebase.route('/homepage')
def homepage():
    current_app.logger.info('Homepage of app')
    return render_template('homepage.html')
