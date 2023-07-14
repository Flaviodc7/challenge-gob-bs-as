import psycopg2 as pg
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return pg.connect(
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            host=config('PGSQL_HOST'),
            port=config('PGSQL_PORT'),
            database=config('PGSQL_DATABASE'),
            sslmode='require'
        )
    except DatabaseError as ex:
        raise ex