# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []

while True:
    arvo = input("Anna arvoja: ")
    luvut.append(arvo)
    if arvo == "":
        break
    print(luvut)

tulos = sorted(luvut, reverse=True)
print(tulos [:5])