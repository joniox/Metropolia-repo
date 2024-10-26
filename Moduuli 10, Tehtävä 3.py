# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self):
        self.alin_kerros = 1
        self.ylin_kerros = 10
        self.nykyinen_kerros = self.alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Olet jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Olet jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Virhe: Kerroksen {kohde_kerros} on oltava välillä {self.alin_kerros} - {self.ylin_kerros}.")
        else:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

class Talo:
    def __init__(self, hissien_lukumäärä):
        self.alin_kerros = 1
        self.ylin_kerros = 10
        self.hissit = [Hissi() for i in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero}.")
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Virhe: Hissi numero {hissin_numero} ei ole olemassa.")

    def palohälytys(self):
        for hissin_numero in range(1, len(self.hissit) + 1):
            print(f"Palohälytys: Hissi {hissin_numero} ajetaan alas.")
            self.aja_hissiä(hissin_numero, self.alin_kerros)

talo = Talo(2)
talo.aja_hissiä(1, 11)
talo.aja_hissiä(2, 7)
talo.palohälytys()