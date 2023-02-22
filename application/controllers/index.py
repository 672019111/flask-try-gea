from application import app
from flask import render_template, url_for, request, redirect, flash, session, jsonify
from application.models.indexModal import *
from application.controllers.handler import *

# controlers untuk ngatur rooter


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/v/moneyTracking')
def moneyTrackingpage():
    return render_template("moneyTracker.html")

@app.route('/note')
def note():
    return render_template("note.html")


# web servis

@app.route('/moneyTracking')
def moneyTracking():
    data = moneyTrackingHandler()
    return jsonify (data)


