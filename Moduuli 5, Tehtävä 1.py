# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

x = []

heitot = int(input("Anna heittojen määrä? "))

import random
for i in range(heitot):
    arpakuutio = random.randint(1, 6)
    x.append(arpakuutio)
print(x)

print("Noppien silmälukujen yhteissumma on:")
print(sum(x))

