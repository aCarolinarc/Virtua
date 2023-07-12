import os
from dotenv import load_dotenv
import mysql.connector

class Data:
    def get_data():
        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        dbcursor = mydb.cursor()
        dbcursor.execute("SELECT * FROM proof")
        resultado = dbcursor.fetchall()
        
        return resultado