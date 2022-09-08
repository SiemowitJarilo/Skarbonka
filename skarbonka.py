import sqlite3

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
    print("3. Dodaj kwote do wszystkich skarbonek ")
    print("4. Dodaj kwote do skarbonki ")
    print("5. Zamknij program ")
    print("*" * 79)
    print("*" * 79)
    choice = int(input("Wybierz opcje: "))
    
    if choice == 1: # Pokaz skarbonkę
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()

        SQL = ''' Select * from dane'''

        cursor.execute(SQL)

        rows = cursor.fetchall()

        for x in rows:
            print("-" * 79)
            print( "ID: ", x[0])
            print( "Nazwa: ", x[1])
            print( "Wartość: ", x[2])
            print('-' * 79)

        cursor.close()

    if choice == 2: # Dodaj skarbonkę
            try:
        
            
                nazwa = input("Podaj nazwę skarbonki: ")
                kwota = int(input("Podaj kwotę skarbonki: "))


                db = sqlite3.connect("simple.db")
                

                SQL = ''' INSERT INTO dane 
                            (nazwa,
                            kwota) 
                            Values ("{}", "{}");'''.format(nazwa, kwota)



                cursor = db.cursor()
                cursor.execute(SQL)
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
    
    if choice == 4: # Dodaj kwote do skarbonki
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        wartość = int(input("Podaj kwote: "))

        SQL = '''SELECT kwota
                 from dane("{}")
                 VALUE (kwota + wartość);'''.format(wartość)

        cursor = db.cursor()
        cursor.execute(SQL)
        db.commit()
        print("Dane dodano poprwanie")
        db.close()
        

    if choice == 5: # Zamknij program 
           break


