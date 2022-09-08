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
    invest_ID   INTEGER,
    FOREIGN KEY(invest_ID) REFERENCES inwestycje(ID)
    );''')        
db.commit
db.close()


print("Skarbonka v0.1")
print("-" * 79)
db = sqlite3.connect("simple.db")
print()
print()
print()

while True:

    print("Menu: ")
    print("1. Pokaż skarbonki ")
    print("2. Dodaj skarbonkę ")
    print("3. Pokaż kwoty Skarbonek ")
    print("4. Dodaj kwote do skarbonki ")
    print("5. Zamknij program ")
    print("*" * 79)
    print("*" * 79)
    print()
    print()
    print()
    choice = int(input("Wybierz opcje: "))
    
    if choice == 1: # Pokaz skarbonkę
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
      
        cursor.execute(''' Select * from inwestycje''')

        rows = cursor.fetchall()

        for x in rows:
            print("-" * 79)
            print( "ID: ", x[0])
            print( "Nazwa: ", x[1])
            print( "Kwota: ", x[2])
            print( "invest_ID: ", x[3])
            print('-' * 79)

        cursor.close()

    if choice == 2: # Dodaj skarbonkę
            try:
        
            
                nazwa = input("Podaj nazwę skarbonki: ")
                wartość = int(input("Podaj kwotę skarbonki: "))
                kwota = int(input("Podaj kwotę pierwszej wpłaty: "))


                db = sqlite3.connect("simple.db")
                
                cursor = db.cursor()
                cursor.execute(''' INSERT INTO inwestycje 
                            (NAZWA,
                            WARTOŚĆ,
                            KWOTA) 
                            Values (?, ?, ?);''', (nazwa, wartość, kwota))
                db.commit()
                print("Dane dodano poprwanie")
                db.close()

            except sqlite3.Error as e:
                print("Error -> Coś poszło nie tak", e)

            finally:
                if (db) :
                    db.close()
                    print("Połączenie zamknięte")
                    print("-" * 79)
    
    if choice == 3: # Pokaż kwoty Skarbonek
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
      
        cursor.execute(''' SELECT 
                                invest_ID,
                                NAZWA, 
                                SUM(KWOTA) 
                            FROM 
                                fundusze
                            GROUP BY NAZWA
        ''')

        rows = cursor.fetchall()

        for x in rows:
            print(x)

        '''for x in rows:
            print("-" * 79)
            print( "ID: ", x[0])
            print( "KWOTA: ", x[1])
            print( "invest_ID: ", x[2])
            print('-' * 79)'''

        cursor.close()

        break

    if choice == 4: # Dodaj kwote do skarbonki
        
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        nazwa = input("Wpisz nazwę: ")
        ilość = int(input("Podaj kwote: "))
        id_invest = int(input("Podaj numer ID Skarbonki: "))

        
        cursor = db.cursor()
        cursor.execute(''' INSERT INTO fundusze
                            (NAZWA, KWOTA, invest_ID) 
                            VALUES (?, ?, ?);''', (nazwa, ilość, id_invest))
        
        db.commit()
        print("Dane dodano poprwanie")
        db.close()
        

    if choice == 5: # Zamknij program 
           break

'''

UPDATE people
SET personal_expense = (
      SELECT SUM(amount)
      FROM expenses
      WHERE expenses.type = 'personal'
        AND expenses.name = people.name ),

    business_expense = (
      SELECT SUM(amount)
      FROM expenses
      WHERE expenses.type = 'business'
        AND expenses.name = people.name )

'''


# cursor.execute('''  UPDATE inwestycje
#                            SET kwota = (?)
#                           WHERE nazwa = (?); ''', (ilość, nazwa))



