import requests
import os
from pyhtml2pdf import converter
from bs4 import BeautifulSoup

def extract(team):
	url = " https://v2.nba.api-sports.io/teams"

	params={
        "name": team}
	headers = {
      'x-apisports-key': '3d8ebfd65da4cbb969179bd4728552d8',
      'x-apisports-host': 'https://v2.nba.api-sports.io/'
    }

	response = requests.request("GET", url, headers=headers, params=params)

	equipo = response.json()
	id = equipo["response"][0]["id"]

	


	#Ahora las estadísticas de la temporada 2022

	url = " https://v2.nba.api-sports.io/teams/statistics"

	params={
        "id": int(id),
		"season": "2022"
	}

	response = requests.request("GET", url, headers=headers, params=params)

	season2022 = response.json()


	#Estadísticas de la temporada 2021 para comparar

	url = " https://v2.nba.api-sports.io/teams/statistics"

	params={
        "id": int(id),
		"season": "2021"
	}

	response = requests.request("GET", url, headers=headers, params=params)

	season2021 = response.json()

	# Jugadores del equipo

	url = " https://v2.nba.api-sports.io/players"

	params={
		"team": int(id),
		"season": "2022"
	}

	response = requests.request("GET", url, headers=headers, params=params)

	jugadores = response.json()

	#Pronóstico usando webscrasping

	page = requests.get('https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/')
	soup = BeautifulSoup(page.text, 'html.parser')

	partidos = soup.find_all(class_="px-box mb-10")
	texto = ""

	#Imprime los próximos partidos con las cuotas
	for partido in partidos:
		texto += partido.text.strip('\n')

	return equipo, season2022, season2021, jugadores, texto

def transform(equipo, season2022, season2021, jugadores, texto):
	#Descargamos el logo del equipo
	logo = equipo["response"][0]["logo"]
	img_data = requests.get(logo).content
	with open('logo.png', 'wb') as f:
		f.write(img_data)
	
	#Otros datos útiles
	code = equipo["response"][0]["code"]
	id = equipo["response"][0]["id"]
	city = equipo["response"][0]["city"]
	nickname = equipo["response"][0]["nickname"]

	#Temporada 2022

	games = season2022["response"][0]["games"]

	fastBreakPoints = season2022["response"][0]["fastBreakPoints"]
	points = season2022["response"][0]["points"]
	biggestLead = season2022["response"][0]["biggestLead"]
	secondChancePoints = season2022["response"][0]["secondChancePoints"]
	pointsOffTurnovers = season2022["response"][0]["pointsOffTurnovers"]
	pointsInPaint = season2022["response"][0]["pointsInPaint"]
	

	fgm = season2022["response"][0]["fgm"]
	fga = season2022["response"][0]["fga"]
	fgp = season2022["response"][0]["fgp"]
	ftm = season2022["response"][0]["ftm"]

	fta = season2022["response"][0]["fta"]
	ftp = season2022["response"][0]["ftp"]
	tpm = season2022["response"][0]["tpm"]
	tpp = season2022["response"][0]["tpp"]

	offReb = season2022["response"][0]["offReb"]
	defReb = season2022["response"][0]["defReb"]
	totReb = season2022["response"][0]["totReb"]

	assists = season2022["response"][0]["assists"]
	pFouls = season2022["response"][0]["pFouls"]
	steals = season2022["response"][0]["steals"]

	turnovers = season2022["response"][0]["turnovers"]
	blocks = season2022["response"][0]["blocks"]
	plusMinus = season2022["response"][0]["plusMinus"]

	#Temporada 2021 para comparar

	games21 = season2021["response"][0]["games"]
	fastBreakPoints21 = season2021["response"][0]["fastBreakPoints"]
	pointsInPaint21 = season2021["response"][0]["pointsInPaint"]
	biggestLead21 = season2021["response"][0]["biggestLead"]
	secondChancePoints21 = season2021["response"][0]["secondChancePoints"]
	pointsOffTurnovers21 = season2021["response"][0]["pointsOffTurnovers"]
	points21 = season2021["response"][0]["points"]
	fgm21 = season2021["response"][0]["fgm"]
	fga21 = season2021["response"][0]["fga"]
	fgp21 = season2021["response"][0]["fgp"]
	ftm21 = season2021["response"][0]["ftm"]
	fta21 = season2021["response"][0]["fta"]
	ftp21 = season2021["response"][0]["ftp"]
	tpm21 = season2021["response"][0]["tpm"]
	tpp21 = season2021["response"][0]["tpp"]
	offReb21 = season2021["response"][0]["offReb"]
	defReb21 = season2021["response"][0]["defReb"]
	totReb21 = season2021["response"][0]["totReb"]
	assists21 = season2021["response"][0]["assists"]
	pFouls21 = season2021["response"][0]["pFouls"]
	steals21 = season2021["response"][0]["steals"]
	turnovers21 = season2021["response"][0]["turnovers"]
	blocks21 = season2021["response"][0]["blocks"]
	plusMinus21 = season2021["response"][0]["plusMinus"]

	#Porcentajes comparando 2021 y 2022

	variables = [team,id,city,nickname,games,fastBreakPoints,points,biggestLead,
	secondChancePoints,pointsOffTurnovers,pointsInPaint,fgm,fga,fgp,ftm,fta,ftp,
	tpm,tpp,offReb,defReb,totReb,assists,pFouls,steals,turnovers,blocks,plusMinus]

	lista22 = [games,fastBreakPoints,points,biggestLead,secondChancePoints,
	pointsOffTurnovers,pointsInPaint,fgm,fga,fgp,ftm,fta,ftp,tpm,tpp,offReb,
	defReb,totReb,assists,pFouls,steals,turnovers,blocks,plusMinus]

	lista21 = [games21,fastBreakPoints21,points21,biggestLead21,secondChancePoints21,
	pointsOffTurnovers21,pointsInPaint21,fgm21,fga21,fgp21,ftm21,fta21,ftp21,tpm21,tpp21,offReb21,
	defReb21,totReb21,assists21,pFouls21,steals21,turnovers21,blocks21,plusMinus21]


	for i in range(len(lista22)):
		variables.append(str(round((float(lista22[i]) - float(lista21[i]))/abs(float(lista21[i]))*100)) + "%")


	#He creado una plantilla html a partir de la cual crear el pdf

	#Variables del html

	for i in range(14):
		variables.append(jugadores['response'][i]['firstname'])
		variables.append(jugadores['response'][i]['lastname'])
		variables.append(jugadores['response'][i]['id'])
		variables.append(jugadores['response'][i]['birth']['date'])
		variables.append(jugadores['response'][i]['birth']['country'])
		variables.append(jugadores['response'][i]['height']['meters'])
		variables.append(jugadores['response'][i]['weight']['kilograms'])
	
	variables.append(texto)

	html = """	
	<!DOCTYPE html>
	<html>
	<body>
		<body style="background-color:rgb(201, 209, 211);">
	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Reporte Temporada 2022-23</h2>
	<h1 style="font-family:Trebuchet MS;text-align:center">{}</h1>
	<img src="logo.png" alt="Logotipo del equipo" width="100px" height="auto" style="position:absolute;top:60px;right:30px">

	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px">ID: {} &emsp; Ciudad: {} &emsp; Apodo: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Temporada 2022-2023</h2>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Partidos jugados: {}</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Fast Break Points: {} &emsp; Points: {} &emsp; Biggest Lead: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Second Chance Points: {} &emsp; Points Off Turnovers: {} &emsp; Points in Paint: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Medidas estadísticas</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FGM: {} &emsp; FGA: {} &emsp; FGP: {} &emsp; FTM: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FTA: {} &emsp; FTP: {} &emsp; TPM: {} &emsp; TPP: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Rebotes</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Offensive Rebounds: {} &emsp; Defensive Rebounds: {} &emsp; Total Rebounds: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Otras estadísticas</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Asistencias: {} &emsp; P-Fouls: {} &emsp; Steals: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Turnovers: {} &emsp; Blocks: {} &emsp; PlusMinus: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Evolución respecto a la temporada anterior</h2>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Partidos jugados: {}</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Fast Break Points: {} &emsp; Points: {} &emsp; Biggest Lead: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Second Chance Points: {} &emsp; Points Off Turnovers: {} &emsp; Points in Paint: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Medidas estadísticas</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FGM:{} &emsp; FGA: {} &emsp; FGP: {} &emsp; FTM: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FTA: {} &emsp; FTP: {} &emsp; TPM: {} &emsp; TPP: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Rebotes</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Offensive Rebounds: {} &emsp; Defensive Rebounds: {} &emsp; Total Rebounds: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Otras estadísticas</h2>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Asistencias: {} &emsp; P-Fouls: {} &emsp; Steals: {}</h3>
	<h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Turnovers: {} &emsp; Blocks: {} &emsp; PlusMinus: {}</h3>

	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Jugadores</h2>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>

	<h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">{} {}, {}</h2>
	<h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: {} &emsp; Nacionalidad: {} &emsp; Altura: {}m &emsp; Peso: {}kg</h3>
	
	<h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Pronóstico próximo partido</h2>
	<h3 style="font-family:Trebuchet MS;text-align:justify;margin:60px 30px 10px">A continuación se pueden ver los próximos partidos y las cuotas de apuestas para el equipo 1 y 2
	Esto nos permite conocer las probabilidades de que gane cada equipo (cuanto más baja es la cuota, mayor es la probabilidad).</h3>
	<h3 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">{}</h3>
	</body>
	</html>

	""".format(*variables) 									
	print(html)
	return html

def load(html):
	with open('report_html.html', "w") as f:
		f.write(html)

	path = os.path.abspath('report_html.html')
	converter.convert(f'file:///{path}', 'report.pdf')


if __name__ == "__main__":
	team = input('Equipo: ')
	equipo, season2022, season2021, jugadores, texto = extract(team)
	html = transform(equipo, season2022, season2021, jugadores,texto)
	load(html)