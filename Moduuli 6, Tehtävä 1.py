# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def arvonta():
    return random.randint(1,6)

while True:
    noppa =  random.randint(1,6)
    print(noppa)
    if noppa == 6:
        break

print(arvonta())