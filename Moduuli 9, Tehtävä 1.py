# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = Auto(rekisteritunnus = "ABC-123", huippunopeus = 142)

print(f"Uuden auton rekisteritunnus on {uusi_auto.rekisteritunnus}.")
print(f"Uuden auton huippunopeus on {uusi_auto.huippunopeus} km/h.")
print(f"Uuden auton tämänhetkinen nopeus on {uusi_auto.tämänhetkinen_nopeus} km/h.")
print(f"Uuden auton kuljettu matka on {uusi_auto.kuljettu_matka} km.")

