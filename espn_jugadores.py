import requests
import selenium
from bs4 import BeautifulSoup

# Requests http a la página espn.com
page = requests.get('http://www.espn.com/nba/players')

soup = BeautifulSoup(page.text, 'html.parser')

partidos = soup.find_all(class_="flex flex-col lg:flex-row justify-around items-center lg:w-full")

#Imprime los próximos partidos
for partido in partidos:
    print(partido.text.strip())

