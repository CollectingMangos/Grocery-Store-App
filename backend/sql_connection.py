import mysql.connector

__connection = None

def get_sql_connection():
    print("Opening mysql connection:")
    global __connection
    if __connection is None:
        __connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='grocery_store')
    return __connection