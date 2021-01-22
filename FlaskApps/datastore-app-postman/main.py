from flask import Flask, request
from google.cloud import datastore
client = datastore.Client()
app = Flask(__name__)


@app.route('/')
def home():
    key = client.key("POSTMAN")
    task = client.get(key)
    return task


@app.route('/login', methods=["POST"])
def loginpage():
    if request.method == "POST":
        req_data = request.get_json()
        key = client.key("POSTMAN", req_data["email"])
        entity = client.get(key)
        usercred = entity.get("email") == req_data["email"] and entity.get("password") == req_data["password"]
        if not usercred:
            return "Wrong Cred"
        return entity


@app.route('/signup', methods=["POST"])
def signuppage():
    with client.transaction():
        req_data = request.get_json()
        key = client.key("POSTMAN", req_data["email"])
        task = datastore.Entity(key=key)
        task.update(
            {
                "name": req_data["name"],
                "email": req_data["email"],
                "password": req_data["password"]
            }
        )
        client.put(task)
    return task

'''
@app.route('/forgotpassword', methods=["GET"])
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
'''

if __name__ == "__main__":
    app.run(debug=True)
