import sqlite3
from sqlite3 import Error


def create_connection(path):
    db_connection = None
    try:
        db_connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return db_connection


def execute_query(db_connection, query):
    cursor = db_connection.cursor()
    try:
        cursor.execute(query)
        db_connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == '__main__':
    print('not designed to be run on its own')
