# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
# arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään
# kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
# sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, aika_tunneissa):
        kuljettu_matka = self.tämänhetkinen_nopeus * aika_tunneissa
        self.kuljettu_matka += kuljettu_matka

class Kilpailu:

    def __init__(self, kilpailun_nimi, pituus_kilometreinä, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_kilometreinä = pituus_kilometreinä
        self.osallistuvat_autot = autot
        self.tunteja_kulunut = 0

    def tunti_kulunut(self):

        while not self.auto_saavuttanut_maalin():
            self.tunteja_kulunut += 1

            for auto in self.osallistuvat_autot:
                auto.kiihdytä(random.randint(-10, 15))

                auto.kulje(1)

            if self.tunteja_kulunut % 10 == 0:
                self.tilanne()

    def tilanne(self):
        for auto in autot:
            print(f"{auto.rekisteritunnus}: Nopeus = {auto.tämänhetkinen_nopeus} km/h, Matka = {auto.kuljettu_matka:.2f} km.")

        print(f"Tunteja kulunut {self.tunteja_kulunut} h")


    def auto_saavuttanut_maalin(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettu_matka >= self.pituus_kilometreinä:
                return True

    def loppuTilanne(self):
        for auto in autot:
            print(f"\nKilpailu on ohi: {auto.rekisteritunnus} on saavuttanut kuljetun matkan {auto.kuljettu_matka} km {self.tunteja_kulunut} tunnissa.")


import random

autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

kilpailu.tunti_kulunut()

kilpailu.loppuTilanne()



