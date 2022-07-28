from src.database import database_handler as db
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database/disbot.sqlite")

connection = db.create_connection(db_path)


def get_user_name_by_id(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE (id = ?)', user_id)
    data = cursor.fetchall()
    return data[0][1]


def get_user_id_by_name(name):
    cursor = connection.cursor()
    name = (name,)
    cursor.execute('SELECT * FROM users WHERE (name = ?)', name)
    data = cursor.fetchall()
    return data[0][1]


if __name__ == '__main__':
    print(get_user_name_by_id('1'))
    print(get_user_id_by_name('Jamie'))
