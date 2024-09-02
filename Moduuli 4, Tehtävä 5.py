# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

käyttäjä = str("python")
salasana = str("rules")
väärät_kerrat = int(5)

while väärät_kerrat > 0:
    käyttäjä = str(input("Mikä on käyttäjätunnus?"))
    salasana = str(input("Mikä on salasana?"))
    if  käyttäjä == "python" and salasana == "rules":
        print ("Tervetuloa!")
    else:
        print("Salasana tai käyttäjä on väärin! Yritä uudestaan.")
        väärät_kerrat = väärät_kerrat - 1