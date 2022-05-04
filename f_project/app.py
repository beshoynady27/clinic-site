from flask import Flask, render_template, request
import sqlite3 

app = Flask(__name__)



@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/book" )
def book():
    
    return render_template("form.html")

@app.route("/booked", methods=["POST", "GET"])
def booked():
    name=request.form.get("name")
    age=request.form.get("age")
    email=request.form.get("email")
    appointment=request.form.get("appointment")
    if not name or not age or not email or not appointment:
        return render_template("failure.html")
    else:
        conn = sqlite3.connect("appo.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO appointments (name, age, email, date) VALUES(?,?,?,?)", (name, age, email, appointment))
        conn.commit()
        conn.close()
        return render_template("success.html", name=name, appointment=appointment)
