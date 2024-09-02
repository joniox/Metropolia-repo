# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

kaupunki = input("Anna ensimmäisen kaupungin nimi: ")
while kaupunki  != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for kaupunki in kaupungit:
    print(kaupunki)