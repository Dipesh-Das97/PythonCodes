from flask import Blueprint, render_template, current_app, Response
import logging
logging.basicConfig(level=logging.DEBUG)
homebase = Blueprint("homebase", __name__, template_folder="templates")
resp = Response()


@homebase.route('/')
def home():
    resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
    current_app.logger.info(resp.headers)
    current_app.logger.info('Starting point of app')
    return render_template('home.html')


@homebase.route('/homepage')
def homepage():
    resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
    current_app.logger.info(resp.headers)
    current_app.logger.info('Homepage of app')
    return render_template('homepage.html')
