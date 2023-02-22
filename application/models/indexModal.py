from application.settings.queryFile import QueryStringDb


def getMoneyTrack():
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
