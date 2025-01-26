from django.db import connection

def query_raw_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM accessLog")
        return cursor.fetchall()
