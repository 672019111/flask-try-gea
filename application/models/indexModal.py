from application.settings.queryFile import QueryStringDb

def getPenerbit():
    customQuery = QueryStringDb()
    query = '''         
        select current_date
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)
