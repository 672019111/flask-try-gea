from application.models.indexModal import *

from flask import request

iduser = '8d1ac791-b9e1-4a0b-95ac-dbddb9cb0c78'
# iduser = '8d1ac791-b9e1-4a0b-95ac-dbddb9cb0c781'

def moneyTrackingHandler():
    result = readMoneyTrack(iduser)['result']
    return result


def addmoneyTrackingHandler():
    nama = request.form['nama']
    nominal = request.form['nominal']

    nominal = int(nominal.replace("Rp. ", "").replace(".", ""))
    result = createMoneyTrack(nama, nominal, iduser)


    return result


def editmoneyTrackingHandler():
    id = request.form['id']
    nominal = request.form['nominal']

    nominal = int(nominal.replace("Rp. ", "").replace(".", ""))

    dataMoneyTracking = readMoneyTrackByID(id)['result']

    SisaBudget = dataMoneyTracking[0]['nominal']
    hasil = SisaBudget-nominal
    result = UpdateMoneyTrack(id, hasil)
    log = CreatelogMoneytrack(id, nominal)
    print (log)
    return result


def deletemoneyTrackingHandler():
    id = request.form['id']

    result = DeleteMoneyTrack(id)
    print(result)

    return result


def resetMoneyTrackingHandler():
    id = request.form['id']
    dataMoneyTracking = readMoneyTrackByID(id)['result']
    budgetAwal = dataMoneyTracking[0]['nominalawal']

    nominal = budgetAwal

    result = UpdateMoneyTrack(id, nominal)
    print(result)

    return result


def DisplayLogMoneyTrackingHandler():
    id = request.form['id']

    result = readlogMoneytrack(id)['result']

    return result
