import requests, sqlite3, json
import pandas as pd

def zonda():
    print("Dostępnę pary:")
    print("1. BTC-PLN")
    print("2. ETH-PLN")
    print("3. BTC-USD")
    print("4. ETH-USD")
    print("5. Inne")
    print("6. Wróć do głównego menu")

    while True:

        choice = int(input('Wybierz parę:'))
        if choice == 1:
            para = "BTC-PLN"
        if choice == 2:
            para = "ETH-PLN"
        if choice == 3:
            para = "BTC-USD"
        if choice == 4:
            para = "ETH-USD"
        if choice == 5:
            para = input("Podaj parę >>XXX-XXX<<: ")
        if choice == 6:
            break

        response = requests.get(f'https://api.zonda.exchange/rest/trading/ticker/{para}')



        if (response.status_code != requests.codes.ok):
            print('coś poszło nie tak')
        else:
            print(json.dumps(response.json(), indent=4))
                        
            """abc = response
            df1 = pd.DataFrame({abc})
            
            print(df1)"""
           
        