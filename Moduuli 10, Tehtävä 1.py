# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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

h = Hissi()
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
