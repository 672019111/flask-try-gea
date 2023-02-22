from application.models.indexModal import *

from flask import request


def moneyTrackingHandler():
    result = readMoneyTrack()['result']
    return result

def addmoneyTrackingHandler():
    nama = request.form['nama']
    nominal = request.form['nominal']

    nominal = int(nominal.replace("Rp. ", "").replace(".", ""))
    
    result = createMoneyTrack(nama, nominal)['result']
    
    return result


def editmoneyTrackingHandler():
    id = request.form['id']
    nominal = request.form['nominal']

    nominal = int(nominal.replace("Rp. ", "").replace(".", ""))

    dataMoneyTracking = readMoneyTrackByID(id)['result']

    SisaBudget = dataMoneyTracking[0]['nominal']
    hasil = SisaBudget-nominal
    result = UpdateMoneyTrack (id, hasil)
    print (result)
    return dataMoneyTracking
    
