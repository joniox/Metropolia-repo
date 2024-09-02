# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

pienin = None
suurin = None

while True:
    luku = input("Anna luku: ")

    if luku == "":
        if pienin is not None and suurin is not None:
            print("Pienin luku on " + str(pienin) + " ja suurin luku on " + str(suurin) + ".")
        break

    try:
        luku = int(luku)

        if pienin is None or suurin is None:
            pienin = suurin = luku
        else:
            pienin = min(pienin, luku)
            suurin = max(suurin, luku)

    except ValueError:
        print("Anna kelvollinen numero.")
