import requests
from xhtml2pdf import pisa

def load(input,output):
	result_file = open(output, "w+b")

	pisa_status = pisa.CreatePDF(input,dest=result_file)

	result_file.close()                

	return pisa_status.err

if __name__ == "__main__":
    html = """ 
    <!DOCTYPE html>
    <html>
    <body>
            <body style="background-color:rgb(201, 209, 211);">
    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Reporte Temporada 2022-23</h2>
    <h1 style="font-family:Trebuchet MS;text-align:center">Los Angeles Lakers</h1>
    <img src="logo.png" alt="Logotipo del equipo" width="150px" height="auto" style="position:fixed;top:60px;right:30px">

    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px">ID: 17 &emsp; Ciudad: Los Angeles &emsp; Apodo: 
    Lakers</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Temporada 2022-2023</h2>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Partidos jugados: 43</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Fast Break Points: 0 &emsp; Points: 4822 &emsp; Biggest Lead: 0</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Second Chance Points: 0 &emsp; Points Off Turnovers: 0 &emsp; Points in Paint: 0</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Medidas estadísticas</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FGM: 1759 &emsp; FGA: 3718 &emsp; FGP: 59.5 &emsp; FTM: 861</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FTA: 1092 &emsp; FTP: 76.8 &emsp; TPM: 443 &emsp; TPP: 32.8</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Rebotes</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Offensive Rebounds: 386 &emsp; Defensive Rebounds: 1521 &emsp; Total Rebounds: 1907</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Otras estadísticas</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Asistencias: 1041 &emsp; P-Fouls: 802 &emsp; Steals: 272</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Turnovers: 640 &emsp; Blocks: 212 &emsp; PlusMinus: -107</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Evolución respecto a la temporada anterior</h2>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Partidos jugados: X</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Fast Break Points: XXXX &emsp; Points: XXXX &emsp; Biggest Lead: XXXX</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Second Chance Points: XXXX &emsp; Points Off Turnovers: XXXX &emsp; Points in Paint: XXXX</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Medidas estadísticas</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FGM:XXXX &emsp; FGA: XXXX 
    &emsp; FGP: XXXX &emsp; FTM: XXXX</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">FTA: XXXX &emsp; FTP: XXXX &emsp; TPM: XXXX &emsp; TPP: XXXX</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Rebotes</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Offensive Rebounds: XXXX &emsp; Defensive Rebounds: XXXX &emsp; Total Rebounds: XXXX</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Otras estadísticas</h2>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Asistencias: XXXX &emsp; P-Fouls: XXXX &emsp; Steals: XXXX</h3>
    <h3 style="background-color:rgb(222, 230, 232);font-family:Trebuchet MS;text-align:center;margin:30px;color:rgb(70, 69, 69)">Turnovers: XXXX &emsp; Blocks: XXXX &emsp; PlusMinus: XXXX</h3>

    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Jugadores</h2>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Damian Jones, 281</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1995-06-30 &emsp; Nacionalidad: USA &emsp; Altura: 2.11m &emsp; Peso: 111.1kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Shaquille Harrison, 626</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1993-10-06 &emsp; Nacionalidad: USA &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Dwayne Bacon, 734</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: None &emsp; Nacionalidad: None &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Thomas Bryant, 753</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1997-07-31 &emsp; Nacionalidad: USA &emsp; Altura: 2.08m &emsp; Peso: 112.5kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Troy Brown Jr., 945</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1999-07-28 &emsp; Nacionalidad: USA &emsp; Altura: 1.98m &emsp; Peso: 97.5kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Lonnie Walker IV, 1038</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1998-12-14 &emsp; Nacionalidad: USA &emsp; Altura: 1.93m &emsp; Peso: 92.5kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Wenyen Gabriel, 970</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1997-03-26 &emsp; Nacionalidad: South Sudan &emsp; Altura: 2.06m &emsp; Peso: 93.0kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Kendrick Nunn, 1007</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1995-08-03 &emsp; Nacionalidad: USA &emsp; Altura: 1.88m &emsp; Peso: 86.2kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Juan Toscano-Anderson, 1934</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: None &emsp; Nacionalidad: None &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Matt Ryan, 3195</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1997-04-17 &emsp; Nacionalidad: USA &emsp; Altura: 2.01m &emsp; Peso: 97.5kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Austin Reaves, 2845</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1998-05-29 &emsp; Nacionalidad: USA &emsp; Altura: 1.96m &emsp; Peso: 89.4kg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Scotty Pippen Jr., 3477</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: None &emsp; Nacionalidad: None &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Jay Huff, 2814</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: 1997-08-25 &emsp; Nacionalidad: USA &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Max Christie, 3427</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: None &emsp; Nacionalidad: None &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>

    <h2 style="font-family:Trebuchet MS;margin:60px 30px 10px">Cole Swider, 3493</h2>
    <h3 style="font-family:Trebuchet MS;margin:10px 30px 60px;color:rgb(70, 69, 69)">Fecha de nacimiento: None &emsp; Nacionalidad: None &emsp; Altura: Nonem &emsp; Peso: Nonekg</h3>


    <h2 style="font-family:Trebuchet MS;text-align:center;margin:60px 30px 10px">Pronóstico próximo partido</h2>

    </body>
    </html>

    """

    load(html,"reporte.pdf")