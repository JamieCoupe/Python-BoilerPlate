import os
from src.database import database_handler as db


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "disbot.sqlite")
table1 = "name of table"
table2 = "name of table2"
connection = db.create_connection(db_path)



def drop_tables():
    drop_statement = 'DROP TABLE {}'

    db.execute_query(connection, drop_statement.format(users))
    db.execute_query(connection, drop_statement.format(insults))
    =


def create_tables():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
    );
    """

    create_insults_table = """
    CREATE TABLE IF NOT EXISTS insults (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      insult TEXT NOT NULL,
      last_used BOOLEAN NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    db.execute_query(connection, create_users_table)
    db.execute_query(connection, create_insults_table)


def populate_tables():
        # Users
        db.execute_query(connection, 'INSERT INTO users  VALUES (1, "Jamie");')
        db.execute_query(connection, 'INSERT INTO users  VALUES (2, "Connor");')

        # Insults
        db.execute_query(connection, 'INSERT INTO insults  VALUES (1, 1, "Are you in the army?", 0);')
        db.execute_query(connection, 'INSERT INTO insults  VALUES (3, 2, "How is italy? I hear it is great this time of'
                                     ' year.", 0);')
        db.execute_query(connection, 'INSERT INTO insults  VALUES (4, 4, "I found a photo from your childhood: https://'
                                     'purpleslobinrecovery.files.wordpress.com/2017/06/4749480-big-teeth-funny-'
                                     'baby-faces.jpg?w=319&h=319&crop=1", 0);')
        db.execute_query(connection, 'INSERT INTO insults  VALUES (9, 6, "Ha", 0);')


if __name__ == '__main__':
    drop = input('Do you wish to drop current tables? ')
    if drop in ['y', 'yes']:
        drop_tables()
    elif drop in ['n', 'no']:
        print('Skipping')
    else:
        print('Not a valid options')

    create = input('Would you like to create new tables? ')
    if create in ['y', 'yes']:
        create_tables()
    elif create in ['n', 'no']:
        print('Skipping')
    else:
        print('Not a valid options')

    populate = input('Would you like to populate defualt data? ')
    if populate in ['y', 'yes']:
        populate_tables()
    elif populate in ['n', 'no']:
        print('Skipping')
    else:
        print('Not a valid options')

