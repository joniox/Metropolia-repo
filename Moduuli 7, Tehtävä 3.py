# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasemat = {"Helsinki-Vantaa": "EFHK", "Arlanda": "ESSA", "Gardermoen": "ENGM"}

while True:
    print("Valitse alla olevista vaihtoehdoista: \n1. Lisää uusi lentoasema\n2. Hae lentoasemaa ICAO-koodilla\n3. Lopetus")
    valinta = input("Syötä valinta (1, 2, 3): ")

    if valinta == '1':
        nimi = input("Anna lentoaseman nimi: ")
        icao = input("Anna lentoaseman ICAO-koodi: ")
        lentoasemat[nimi] = icao
        print(f"Lentoasema {nimi} on lisätty ICAO-koodilla {icao}.")

    elif valinta == '2':
        icao_koodi = input("Anna ICAO-koodi: ")
        for nimi, icao in lentoasemat.items():
            if icao == icao_koodi:
                print(f"Lentoasema: {nimi}, ICAO: {icao}")
                break
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == '3':
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")




