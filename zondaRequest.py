import requests, sqlite3, json

def zonda():
    print("Dostępnę pary:")
    print("1. BTC-PLN")
    print("2. ETH-PLN")
    print("3. BTC-USD")
    print("4. ETH-USD")
    print("5. Zamknij aplikację")

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
            break


        response = requests.get(f'https://api.zonda.exchange/rest/trading/ticker/{para}')

        if (response.status_code != requests.codes.ok):
            print('coś poszło nie tak')
        else:
            print(json.dumps(response.json(), indent=4))