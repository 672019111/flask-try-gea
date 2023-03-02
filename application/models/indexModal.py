from application.settings.queryFile import QueryStringDb


def readMoneyTrack(iduser):
    customQuery = QueryStringDb()
    query = '''         
    SELECT 
        id, 
        nama, 
        nominal, 
        nominalawal 
    FROM 
        moneytrack m 
    WHERE 
        iduser = %(iduser)s
    ORDER BY 
        id;
            '''
    kondisi = {
        'iduser': iduser

    }
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


def createMoneyTrack(nama, nominal, iduser):
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
            %(nominal)s,
            %(iduser)s,

            );
            '''
    kondisi = {
        'nama': nama,
        'nominal': nominal,
        'iduser': iduser

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


def CreatelogMoneytrack(id, nominal,):
    customQuery = QueryStringDb()
    query = '''         
        INSERT INTO logMoneytrack 
            (keterangan, nominal, idmoneytrack) 
        VALUES 
            (%(keterangan)s, %(nominal)s, %(id)s)
            '''
    kondisi = {
        'id': id,
        'keterangan': 'null',
        'nominal': nominal,
    }
    return customQuery.execute(query, kondisi)

def readlogMoneytrack(id):
    customQuery = QueryStringDb()
    query = '''         
        select 
            keterangan, 
            nominal, 
            tanggal 
        from 
            logMoneytrack
        where 
            idmoneytrack = %(id)s
        order by 
            tanggal desc 
            '''
    kondisi = {
        'id': id,

    }
    return customQuery.select(query, kondisi)
