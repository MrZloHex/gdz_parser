import sqlite3


def init():
    conn = sqlite3.connect('gdz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gdz (klass INT, lesson TEXT, name_book TEXT);''')
    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect('gdz.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS gdz;''')
    conn.commit()
    conn.close()


def insert(klass: int, lesson: str, name_book: str):
    conn = sqlite3.connect('gdz.db')
    c = conn.cursor()
    c.execute('''INSERT INTO gdz VALUES (?, ?, ?);''', [klass, lesson, name_book])
    conn.commit()
    conn.close()
