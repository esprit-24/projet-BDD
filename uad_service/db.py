import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="site_uad",
        user="postgres",
        password="postgres"
    )
