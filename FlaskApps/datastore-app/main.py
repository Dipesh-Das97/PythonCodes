from flask import Flask
import logging
from admin.homebase import homebase
from admin.loginpage import loginpage
from admin.signuppage import signuppage
from admin.logoutpage import logoutpage
from admin.forgotpasswordpage import forgotpasswordpage
from admin.deletepage import deletepage
from admin.errorhandlerpage import errorhandlerpage
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.secret_key = "SUPER_SECRET"
app.register_blueprint(homebase)
app.register_blueprint(loginpage)
app.register_blueprint(signuppage)
app.register_blueprint(logoutpage)
app.register_blueprint(forgotpasswordpage)
app.register_blueprint(deletepage)
app.register_blueprint(errorhandlerpage)

if __name__ == "__main__":
    app.run(debug=True)
