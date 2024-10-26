# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
# ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan
# hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde_kerros)  # Käytetään hissien indeksit alkaen 0
        else:
            print(f"Virhe: Hissi numero {hissin_numero} ei ole olemassa.")

talo = Talo(2)
talo.aja_hissiä(1, 11)
talo.aja_hissiä(2, 7)



