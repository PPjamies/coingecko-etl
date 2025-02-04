import os

import psycopg2
from psycopg2 import sql

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pwrd = os.getenv('DB_PWRD')

if not db_host:
    raise ValueError("Missing environment variable: DB_HOST")
if not db_port:
    raise ValueError("Missing environment variable: DB_PORT")
if not db_name:
    raise ValueError("Missing environment variable: DB_NAME")
if not db_user:
    raise ValueError("Missing environment variable: DB_USER")
if not db_pwrd:
    raise ValueError("Missing environment variable: DB_PWRD")


def init_postgres():
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_pwrd,
        )
        print("Database connection established")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None


def load_bulk_to_postgres(conn, table, columns, data):
    try:
        with conn.cursor as cursor:
            query = sql.SQL(
                "INSERT INTO {table} ({fields}) VALUES ({values})".format(
                    table=sql.Identifier(table),
                    fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
                    values=sql.SQL(', ').join(sql.Placeholder() * len(columns))
                )
            )
            cursor.executemany(query, data)
            conn.commit()
            print("Data loaded successfully")
    except Exception as e:
        print(f"Error during data loading: {e}")
        conn.rollback()
    finally:
        pass
