from flask import Flask, render_template, request, redirect, session, url_for
from google.cloud import datastore
client = datastore.Client()
app = Flask(__name__)
app.secret_key = "SUPER_SECRET"
database = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/homepage/login', methods=["GET", "POST"])
def loginpage():
    if request.method == "POST":
        key = client.key("AUTH", request.form["email"])
        entity = client.get(key)
        usercred = entity.get("email") == request.form["email"] and entity.get("password") == request.form["password"]
        if usercred:
            session["user"] = request.form["email"]
            return redirect(url_for("postlog"))
        else:
            return redirect("/homepage/signup")
    return render_template("login.html")


@app.route('/homepage/postlogin')
def postlog():
    if "user" in session:
        return render_template("postlogin.html")
    return redirect('/homepage/login')


@app.route('/homepage/signup', methods=["GET", "POST"])
def signuppage():
    if request.method == "POST":
        with client.transaction():
            key = client.key("AUTH", request.form["email"])
            task = datastore.Entity(key=key)
            task.update(
                {
                    "name": request.form["name"],
                    "email": request.form["email"],
                    "password": request.form["password"]
                }
            )
            client.put(task)
        return redirect('/homepage/login')
    return render_template('signup.html')


@app.route('/homepage/logout')
def logoutpage():
    session.pop("user", None)
    return render_template('logout.html')


@app.route('/homepage/forgotpassword', methods=["GET", "POST"])
def forgotpass():
    if request.method == "POST":
        with client.transaction():
            key = client.key("AUTH", request.form["email"])
            entity = client.get(key)
            if not entity.get("email") == request.form["email"] and request.form["password"]:
                return "Wrong Email or enter new password again"
            entity["password"] = request.form["password"]
            client.put(entity)
        return redirect('/homepage/login')
    return render_template("forgotpassword.html")


@app.route('/homepage/delete', methods=["GET", "POST"])
def removeacc():
    if request.method == "POST":
        key = client.key("AUTH", request.form["email"])
        client.delete(key)
        return redirect('/homepage')
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
