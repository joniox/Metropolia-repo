# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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

import random

autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

tunteja_kulunut = 0
auto_saavuttanut_maalin = False

while not auto_saavuttanut_maalin:
    tunteja_kulunut += 1

    for auto in autot:
        auto.kiihdytä(random.randint(-10,15))

        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            auto_saavuttanut_maalin = True
            voittoauto = auto
            break

for auto in autot:
   print(f"{auto.rekisteritunnus}: Huippunopeus = {auto.huippunopeus} km/h, Matka = {auto.kuljettu_matka:.2f} km")

print(f"\nKilpailu on ohi: {voittoauto.rekisteritunnus} on saavuttanut maalin 10,000 km {tunteja_kulunut} tunnissa.")

