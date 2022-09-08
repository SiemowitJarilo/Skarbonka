import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE dane(
    ID integer primary key AUTOINCREMENT,
    nazwa string,
    kwota integer)
        
''')


db.commit
db.close()
