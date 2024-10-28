# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
# ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Kirja:

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"{self.nimi}: {self.kirjoittaja}: {self.sivumaara}")

class Lehti:

    def __init__(self, nimi, paatoimittaja):
        self.nimi = nimi
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi}: {self.paatoimittaja}")

lehtijulkaisu = Lehti("Aku Ankka", "Aki Hyyppä")
kirjajulkaisu = Kirja("Hytti n:o 6", "Rosa Liksom", 200 )

lehtijulkaisu.tulosta_tiedot()
kirjajulkaisu.tulosta_tiedot()