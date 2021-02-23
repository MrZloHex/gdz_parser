import sqlite3


# method of creation a table in db
def init():
    with sqlite3.connect('gdz.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS gdz (klass INT, lesson TEXT, name_book TEXT, authors TEXT, type TEXT, 
                     year INT, img TEXT);''')
        conn.commit()
    conn.close()


# method of clearing any table in db
def delete():
    with sqlite3.connect('gdz.db') as conn:
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS gdz;''')
        conn.commit()
    conn.close()


# method of inserting data in table
def insert(klass: int, lesson: str, name_book: str, authors: str, tip: str, year: int, img: str):
    with sqlite3.connect('gdz.db') as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO gdz VALUES (?, ?, ?, ?, ?, ?, ?);''',
                  [klass, lesson, name_book, authors, tip, year, img])
        conn.commit()
    conn.close()
