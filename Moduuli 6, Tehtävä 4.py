# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(numerot):
    summa = sum(numerot)
    return summa

numerot = [43, 32, 42, 65, 3, 99]

summa = summa(numerot)

print("Lukujen summa on " + str(summa) + ".")