# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='root_pw',
         autocommit=True
         )

def lentokenttien_lukumäärät_tyypeittäin(maakoodi):
    sql = f"SELECT type, iso_country FROM airport where iso_country = '{maakoodi}' "
#    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    pieni = keskisuuri = suuri = helikopteri = suljettu = 0
    if kursori.rowcount > 0:
        for rivi in tulos:
            if rivi[0] == "small_airport":
                pieni += 1
            elif rivi[0] == "medium_airport":
                keskisuuri += 1
            elif rivi[0] == "large_airport":
                suuri += 1
            elif rivi[0] == "heliport":
                helikopteri += 1
            elif rivi[0] == "closed":
                suljettu += 1
        print(f"Pieniä lentokenttiä on {pieni} , keskisuuria lentokenttiä on {keskisuuri} , isoja lentokenttiä on {suuri} , helikopterikenttiä on {helikopteri} ja suljettuja kenttiä on {suljettu}.")
    return

maakoodi = input("Anna maakoodi: ")
lentokenttien_lukumäärät_tyypeittäin(maakoodi)