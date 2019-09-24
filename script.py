#!/usr/bin/env python

from flask import Flask, request, render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = 'shhdonttell'

@app.route("/home")
def trashapp():
	return render_template("home.html")

@app.route("/report")
def home():
	return render_template("report.html")


@app.route("/map")
def map():
	return render_template("map.html")


@app.route("/table")
def table():
	return render_template("table.html")

@app.route("/resolve/<id>")
def report(id):
	post_id = str(id)
	return render_template("resolve.html", post_id = post_id)


@app.route("/past")
def past():
	return render_template("past.html")

@app.route("/header")
def header():
	return render_template("header.html")


if __name__ == "__main__":
	app.run(debug=True)