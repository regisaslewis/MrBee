import sqlite3

conn = sqlite3.connect("sql_database.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS successful_guesses
    (date text NOT NULL, word text)''')

conn.commit()