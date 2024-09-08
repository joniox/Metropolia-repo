# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

luvut = [21, 23, 24, 25, 26, 27]

def karsi_parittomat(luvut):
    return [numero for numero in luvut if numero % 2 == 0]

karsittu_lukulista = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu_lukulista)

