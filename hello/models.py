from django.db import models, connection

class MyModel(models.Model):
    # Define your fields here

    @staticmethod
    def query_raw_sql():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM accessLog")
            return cursor.fetchall()
