from application.settings.queryFile import QueryStringDb


def readMoneyTrack():
    customQuery = QueryStringDb()
    query = '''         
        select 
            id, 
            nama, 
            nominal, 
            nominalawal 
        from 
            moneytrack m 
        order by 
            id
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def readMoneyTrackByID(id):
    customQuery = QueryStringDb()
    query = '''         
        select 
            id, 
            nama, 
            nominal, 
            nominalawal 
        from 
            moneytrack m 
        where 
            id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)


def createMoneyTrack(nama, nominal):
    customQuery = QueryStringDb()
    query = '''         
        INSERT INTO 
            moneytrack (
                nama, 
                nominal, 
                nominalawal
                )
        VALUES (
            %(nama)s, 
            %(nominal)s, 
            %(nominal)s
            );
            '''
    kondisi = {
        'nama': nama,
        'nominal': nominal

    }
    return customQuery.execute(query, kondisi)


def UpdateMoneyTrack(id, nominal):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE moneytrack
        SET nominal = %(nominal)s
        WHERE id = %(id)s;
            '''
    kondisi = {
        'id': id,
        'nominal': nominal

    }
    return customQuery.execute(query, kondisi)


def DeleteMoneyTrack(id):
    customQuery = QueryStringDb()
    query = '''         
        DELETE FROM 
            moneytrack
        WHERE 
            id = %(id)s;
            '''
    kondisi = {
        'id': id,

    }
    return customQuery.execute(query, kondisi)
