from src.database.db import get_connection
from .entities.Estacion import Estacion
from .entities.EstacionAdd import EstacionAdd

class EstacionModelo():

    @classmethod
    def get_estaciones(self):
        try:
            connection = get_connection()
            estaciones = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, location FROM weather_stations ORDER BY id")
                resultset = cursor.fetchall()

                for row in resultset:
                    estacion = Estacion(row[0], row[1], row[2])
                    estaciones.append(estacion.to_JSON())

            connection.close()
            return estaciones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_estacion(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, location FROM weather_stations WHERE id = %s", (id))
                row = cursor.fetchone()

                estacion = None

                if row != None:
                    estacion = Estacion(row[0], row[1], row[2])
                    estacion = estacion.to_JSON()

            connection.close()
            return estacion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_estacion(self, estacion):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO weather_stations (name, location) 
                VALUES (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))""", (estacion.name, estacion.latitude, estacion.longitude))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_estacion(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM weather_stations WHERE id = %s", (id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_estacion(self, estacion):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE weather_stations SET name = %s, location = ST_SetSRID(ST_MakePoint(%s, %s), 4326) WHERE id = %s""", (estacion.name, estacion.latitude, estacion.longitude, estacion.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)