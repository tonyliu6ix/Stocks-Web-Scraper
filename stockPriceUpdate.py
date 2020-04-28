import requests
import bs4
from bs4 import BeautifulSoup
import os


def parse_price():
    r1 = requests.get("https://finance.yahoo.com/quote/FB?p=FB")
    r2 = requests.get("https://finance.yahoo.com/quote/GOOGL/")
    soup1 = BeautifulSoup(r1.text, "html.parser")
    soup2 = BeautifulSoup(r2.text, "html.parser")
    fb_price = soup1.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    googl_price = soup2.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return fb_price, googl_price


os.system("cls")

while True:
    fb_price, googl_price = parse_price()
    print("FB: " + fb_price + " USD" + " | " + "GOOGL: " + googl_price + " USD")

