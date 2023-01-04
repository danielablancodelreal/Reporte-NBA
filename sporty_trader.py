import requests
from bs4 import BeautifulSoup

# Requests http a la página sportytrader.es
page = requests.get('https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/')

soup = BeautifulSoup(page.text, 'html.parser')

partidos = soup.find_all(class_="px-box mb-10")

#Imprime los próximos partidos con las cuotas
for partido in partidos:
    print(partido.text.strip('\n'))

