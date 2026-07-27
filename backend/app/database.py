import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
dbname = os.getenv("POSTGRES_DB")


def get_db():
    conn = psycopg.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        row_factory=dict_row,
    )
    try:
        yield conn

    finally:
        conn.close()
