from application import app
from flask import render_template, url_for, request, redirect, flash, session


@app.route('/')
def home():
    return render_template("index.html")
