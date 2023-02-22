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
def jsonify_response(status_code, status, message=None, data=None):
    response = {
        'status_code': status_code,
        'status': status,
        'message': message
    }
    if data:
        response['data'] = data
    return jsonify(response)


@app.route('/moneyTracking', methods=['GET', 'POST', 'PUT'])
def moneyTracking():
    result = moneyTrackingHandler()
    if request.method == 'POST':
        result = addmoneyTrackingHandler()
        return jsonify_response(201, 'Success', 'CREATED', result)
    if request.method == 'PUT':
        result = editmoneyTrackingHandler()
        return jsonify_response(200, 'Success', 'ok', result)

    return jsonify_response(200, 'Success', 'Ok', result)
