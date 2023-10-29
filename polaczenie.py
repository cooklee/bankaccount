import psycopg2

settings = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'vetjopoco',
    'database':'bank',
}
def connect():
    connection = psycopg2.connect(**settings)
    connection.autocommit = True
    return connection