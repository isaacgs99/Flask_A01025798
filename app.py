from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient, cursor

con = MongoClient("localhost", 2700)
db = con.Escuela
cuentas = db.alumno

app = Flask(__name__)


@app.route("/")
def index():
    cursor = cuentas.find()
    user = []
    for doc in cursor:
        user.append(doc)
    return render_template("/user.html", data=user)


@app.route("/user", methods=["POST"])
def user():
    return render_template("/user.html", data=request.form["password"])


@app.route("/home/")
def home():
    return render_template("/index.html")

# GET


# @app.route("/test/<data>")
# def test(data):
#     return "hola %s" % data


if __name__ == "__main__":
    app.run(debug=True)
