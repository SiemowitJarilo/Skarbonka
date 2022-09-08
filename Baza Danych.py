import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS inwestycje(
    ID          INTEGER     PRIMARY KEY     AUTOINCREMENT,
    NAZWA       STRING,
    WARTOŚĆ     INTEGER,
    KWOTA       INTEGER)
        ''')

cursor.execute('''

    CREATE TABLE IF NOT EXISTS fundusze(
    ID          INTEGER     PRIMARY KEY     AUTOINCREMENT,
    NAZWA       STRING,
    KWOTA       INTEGER,
    INVEST_ID   INTEGER     NOT NULL,
    FOREIGN KEY(invest_ID) REFERENCES inwestycje(ID)
    );''')        

db.commit
db.close()
