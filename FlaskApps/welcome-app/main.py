from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods=["GET"])
def welcome():
    return "Hello World!"


@app.route('/hello/<string:name>')
def name_calling(name):
    return "Welcome " + name


if __name__ == '__main__':
    app.run(debug=True)
