from application.settings.queryFile import QueryStringDb

def getPenerbit():
    customQuery = QueryStringDb()
    query = '''         
        select * from penerbit
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)
