from database.db import get_connection
from .entities.Estacion import Estacion

class EstacionModelo():

    def get_estacion(self):
        try:
            connection=get_connection()
            estaciones=[]

            with connection.cursor() as cursor:
                cursor.execute('SELECT ')
        except: Exception as ex:
            raise Exception(ex)