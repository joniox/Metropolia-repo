# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien
# välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='root_pw',
         autocommit=True
         )

def haekoordinaatit(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao = input("Anna ensimmäinen ICAO: ")
koordinaatti1 = haekoordinaatit(icao)
icao = input("Anna toinen ICAO: ")
koordinaatti2 = haekoordinaatit(icao)

print(koordinaatti1, koordinaatti2)

print(f"Etäisyys annettujen lentokenttien välillä on {distance.distance(koordinaatti1, koordinaatti2).km:.2f}")

