import sqlite3

conn = sqlite3.connect("sql_database.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS successful_guesses
    (date text NOT NULL, word text)''')

cursor.execute("INSERT INTO successful_guesses VALUES ('2025-02-01', 'horses')")
cursor.execute("INSERT INTO successful_guesses VALUES ('2025-02-01', 'shores')")
cursor.execute("INSERT INTO successful_guesses VALUES ('2025-02-01', 'roses')")

table = cursor.execute('''SELECT * FROM successful_guesses''')
for row in table:
    print(row)
    
conn.commit()
conn.close()