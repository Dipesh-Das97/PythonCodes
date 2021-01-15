from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

base = [
    {
        "id": 1,
        "name": "Dipesh Das",
        "designation": "Junior Software Engineer"
    },
    {
        "id": 2,
        "name": "Jaikishan",
        "designation": "Software Engineer"
    },
    {
        "id": 3,
        "name": "Kamesh",
        "designation": "Team Lead"
    }
]


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/home/database')
def database():
    return jsonify(base)


@app.route('/home/database/<int:empid>')
def employee_detail(empid):
    if request.method == "GET":
        newlist = [x for x in base if x.get("id") == empid]
        return jsonify(newlist)


@app.route('/home/database', methods=["POST"])
def new_details():
    if request.method == "POST":
        print("This is POST")
        req_data = request.get_json()
        newempdetails = {
            "id": len(base) + 1,
            "name": req_data["name"],
            "designation": req_data["designation"]
        }
        base.append(newempdetails)
        return newempdetails


@app.route('/home/database/<int:empid>', methods=["PUT"])
def update_details(empid):
    if request.method == "PUT":
        print("This is PUT")
        derivedlist = [x for x in base if x.get("id") == empid]
        if not derivedlist:
            print("Not available")
            return "Wrong ID"
        updatelist = base[empid-1]
        base.remove(updatelist)
        req_data = request.get_json()
        updatelist["name"] = req_data["name"]
        base.insert(empid-1, updatelist)
        return updatelist


@app.route('/home/database/<int:empid>', methods=["DELETE"])
def delete_details(empid):
    if request.method == "DELETE":
        print("This is DELETE")
        derivedlist = [x for x in base if x.get("id") == empid]
        if not derivedlist:
            print("Not available")
            return "Wrong ID"
        base.pop(empid-1)
        return jsonify(base)


if __name__ == '__main__':
    app.run(debug=True)
