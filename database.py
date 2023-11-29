import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import mysql.connector 

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')

def select(query):
    print("Intentando conectar a la base de datos...")
    try:
        with mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            port=DB_PORT
        ) as connector:
            with connector.cursor() as cursor:
                cursor.execute(query)
                num_filas_afectadas = cursor.rowcount
                connector.commit()
                print(f"Operación de inserción exitosa. Filas afectadas: {num_filas_afectadas}")
                return num_filas_afectadas
    except mysql.connector.Error as err:
        print(f"Error de MySQL durante la inserción: {err}")
