from application import app
from flask import render_template, url_for, request, redirect, flash, session, jsonify
from application.models.indexModal import *
from application.controllers.MoneyTrackinghandler import *
from application.controllers.outhHandler import *

# controlers untuk ngatur rooter


@app.route('/')
# @usersLoginRequired
def home():
    # return redirect(url_for('moneyTrackingpage'))
    # return render_template("index.html")
    return render_template("layout.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("udah disini ")
        login = loginHandler()
        if login['status'] == True:
            print("true", login)
            return redirect(url_for('home'))
        else:
            print(login)
            return redirect(url_for('login'))
    # return redirect(url_for('login'))
    return render_template("outh/login.html")


@app.route('/v/moneyTracking')
# @usersLoginRequired
def moneyTrackingpage():
    return render_template("moneyTracker.html")


@app.route('/note')
def note():
    return render_template("note.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

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


@app.route('/moneyTracking', methods=['GET', 'POST', 'PUT', 'DELETE'])
def moneyTracking():
    result = moneyTrackingHandler()
    if request.method == 'POST':
        result = addmoneyTrackingHandler()
        return jsonify_response(201, 'Success', 'CREATED', result)
    if request.method == 'PUT':
        result = editmoneyTrackingHandler()
        return jsonify_response(200, 'Success', 'ok', result)
    if request.method == 'DELETE':
        result = deletemoneyTrackingHandler()
        return jsonify_response(200, 'Success', 'ok', result)

    return jsonify_response(200, 'Success', 'Ok', result)


@app.route('/moneyTracking/reset', methods=['POST'])
def resetmoneyTracking():
    result = resetMoneyTrackingHandler()
    return jsonify_response(200, 'Success', 'Ok', result)


@app.route('/moneyTracking/history', methods=['POST'])
def historymoneyTracking():
    result = [
        {'tanggal': '2022-01-01', 'nominal': 1000000,
         'keterangan': 'Pembayaran Gaji'},
        {'tanggal': '2022-01-05',    'nominal': 250000,
            'keterangan': 'Pembelian Bahan Baku'},
        {'tanggal': '2022-01-15',   'nominal': 750000,
            'keterangan': 'Pembayaran Sewa'},
        {'tanggal': '2022-02-01', 'nominal': 1250000,
            'keterangan': 'Pembayaran Gaji'},
        {'tanggal': '2022-02-05',    'nominal': 350000,
            'keterangan': 'Pembelian Bahan Baku'},
        {'tanggal': '2022-02-15',   'nominal': 1000000, 'keterangan': 'Pembayaran Sewa'}]

    return jsonify_response(200, 'Success', 'Ok', result)
