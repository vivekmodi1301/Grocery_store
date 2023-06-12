import mysql.connector

def get_sql_connection():
    __cxn = None
    if __cxn is None: 
        __cxn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Vivek@131",
                database="gs"
            )
    return __cxn