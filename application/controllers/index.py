from application import app
from flask import render_template, url_for, request, redirect, flash, session, jsonify
from application.models.indexModal import *

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/i')
def iphone():
    data = getPenerbit()
    return jsonify(data)
