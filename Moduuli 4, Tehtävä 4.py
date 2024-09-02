# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

nro = random.randint(1,10)
nro_str = str(nro)

while True:

    arvaus = int(input("Mikä on oikea numero? "))
    if arvaus < nro:
        print("Arvasit liian pienen numeron")
    elif arvaus > nro:
        print("Arvasit liian suuren numeron")
    else:
        print("Arvasit oikein!")
        break