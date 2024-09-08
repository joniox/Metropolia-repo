# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def arvonta(tahkojen_määrä):
    return random.randint(1, tahkojen_määrä)

while True:
    tahkojen_määrä = int(input("Anna tahkojen määrä: "))
    maksimi_silmäluku = tahkojen_määrä
    silmäluku = 0

    while silmäluku != maksimi_silmäluku:
        silmäluku = arvonta(tahkojen_määrä)
        print(f"Heitto: {silmäluku}")
