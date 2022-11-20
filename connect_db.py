import sqlite3


def create_db():
    with open('create_database.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('education.db') as conn:
        c = conn.cursor()
        c.executescript(sql)
        print('Database created!')


if __name__ == '__main__':
    create_db()
