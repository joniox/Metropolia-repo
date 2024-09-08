# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

talvi = str(12), str(1), str(2)
kevät = str(3), str(4), str(5)
kesä = str(6), str(7), str(8)
syksy = str(9), str(10), str(11)

kuukausi = int(input("Anna kuukauden numero 1-12: "))

if str(kuukausi) in talvi:
    print("Kuukautta vastaava vuodenaika on talvi.")
elif str(kuukausi) in kevät:
    print("Kuukautta vastaava vuodenaika on kevät.")
elif str(kuukausi) in kesä:
    print("Kuukautta vastaava vuodenaika on kesä.")
elif str(kuukausi) in syksy:
    print("Kuukautta vastaava vuodenaika on syksy.")
else:
    print("Virheellinen kuukausi.")
