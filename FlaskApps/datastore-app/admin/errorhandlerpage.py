from flask import Blueprint, render_template, Response
response = Response()
errorhandlerpage = Blueprint("errorhandlerpage", __name__, template_folder="templates")


"""
    this script handles 2 errors: 404 page not found error and 500 server/app error with the rendered templates
"""


@errorhandlerpage.app_errorhandler(404)
def pagenotfound(e):
    current_app.logger.info('Response header linked: %s', response.headers)
    return render_template("errorhandler.html")


@errorhandlerpage.app_errorhandler(500)
def servererror(e):
    current_app.logger.info('Response header linked: %s', response.headers)
    return render_template("servererror.html")
