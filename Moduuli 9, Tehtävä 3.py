# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 60
        self.kuljettu_matka = 2000

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, aika_tunneissa):
        kuljettu_matka = self.tämänhetkinen_nopeus * aika_tunneissa
        self.kuljettu_matka += kuljettu_matka


uusi_auto = Auto(rekisteritunnus = "ABC-123", huippunopeus = 142)

print(f"Kuljettu matka ensin on {uusi_auto.kuljettu_matka} km.")

uusi_auto.kulje(1.5)

print(f"Kuljettu matka lisämatkan jälkeen on {uusi_auto.kuljettu_matka} km.")

