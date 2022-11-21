import sqlite3


def create_db(setup_file, database):
    with open(setup_file) as f:
        sql = f.read()

    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        c.executescript(sql)
        print('Database created!')
