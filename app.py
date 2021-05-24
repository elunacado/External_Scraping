from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def code():
    what = input("¿Que cripto moneda quieres calcular? ETH, BTC o DOGE   ")

    def ETH():
        print()

        print("ETHEREUM PRICE CALCULATOR: ")
        coindesk = requests.get("https://www.coindesk.com/price/ethereum").text
        soup = BeautifulSoup(coindesk, "lxml")
        now = datetime.now()

        ethereum=soup.find("div", class_="price-large")
        ethereum_price=ethereum.text
        print(ethereum_price)
        print(now.hour,":",now.minute,":",now.second)

    def BTC():
        print()
        print("BITCOIN PRICE CALCULATOR: ")
        coindesk = requests.get("https://www.coindesk.com/price/bitcoin").text
        soup = BeautifulSoup(coindesk, "lxml")
        now = datetime.now()

        bitcoin=soup.find("div", class_="price-large")
        bitcoin_price=bitcoin.text
        print(bitcoin_price)
        print(now.hour,":",now.minute,":",now.second)

    def DGC():
        print()
        print("DOGECOIN PRICE CALCULATOR: ")
        coindesk = requests.get("https://www.coindesk.com/price/dogecoin").text
        soup = BeautifulSoup(coindesk, "lxml")
        now = datetime.now()

        dogecoin=soup.find("div", class_="price-large")
        dogecoin_price=dogecoin.text
        print(dogecoin_price)
        print(now.hour,":",now.minute,":",now.second)

    if __name__=='__main__' and what=="DOGE":
        while True:
            DGC()
            time_wait = 1
            print(f'Waiting {time_wait} minute...')
            time.sleep(time_wait * 60)

    elif __name__=='__main__' and what=="BTC":
        while True:
            BTC()
            time_wait = 1
            print(f'Waiting {time_wait} minute...')
            time.sleep(time_wait * 60)

    elif __name__=='__main__' and what=="ETH":
        while True:
            ETH()
            time_wait = 1
            print(f'Waiting {time_wait} minute...')
            time.sleep(time_wait * 60)

    else:
        print("perdon pero ingresa una cripto valida")
        code()
code()


