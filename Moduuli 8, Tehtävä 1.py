# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='root_pw',
         autocommit=True
         )

def hae_lentokentän_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport where ident = '{icao}' "
#    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja kunta on {rivi[1]}")
    return

icao = input("Anna lentokentä icao-koodi: ")
hae_lentokentän_tiedot(icao)


