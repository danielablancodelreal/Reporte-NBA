import requests
from bs4 import BeautifulSoup

# Requests http a la página sportytrader.es
page = requests.get('https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/')

soup = BeautifulSoup(page.text, 'html.parser')

partidos = soup.find_all(class_="flex flex-col lg:flex-row justify-around items-center lg:w-full")

#Imprime los próximos partidos
for partido in partidos:
    print(partido.text.strip())

