from application.models.indexModal import *

def moneyTrackingHandler():

    # data = getMoneyTrack()['result']
    data = [{'id': 1, 'nama': 'Belanja bulanan', 'nominal': 1500000, 'nominalawal': 0},
            {'id': 2, 'nama': 'Makan siang', 'nominal': 50000, 'nominalawal': 0},
            {'id': 3, 'nama': 'Beli buku', 'nominal': 75000, 'nominalawal': 0},
            {'id': 4, 'nama': 'Bayar listrik', 'nominal': 500000, 'nominalawal': 0},
            {'id': 5, 'nama': 'Pembayaran hutang', 'nominal': 1000000, 'nominalawal': 0}]
    return data
