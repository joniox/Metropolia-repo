# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pizzan_yksikköhinta(halkaisija, hinta):
    säde = halkaisija / 2
    pinta_ala = math.pi * (säde / 100) **2
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

ensimmäisen_pizzan_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
ensimmäisen_pizzan_hinta = float(input("Anna ensimmäisen pizzan hinta euroina: "))

toisen_pizzan_halkaisija = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
toisen_pizzan_hinta = float(input("Anna toisen pizzan hinta euroina: "))

ensimmäisen_pizzan_yksikköhinta = pizzan_yksikköhinta(ensimmäisen_pizzan_halkaisija, ensimmäisen_pizzan_hinta)
toisen_pizzan_yksikköhinta = pizzan_yksikköhinta(toisen_pizzan_halkaisija, toisen_pizzan_hinta)

if ensimmäisen_pizzan_yksikköhinta < toisen_pizzan_yksikköhinta:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahalle. Yksikköhinta: {ensimmäisen_pizzan_yksikköhinta:.2f} €/m²")
elif ensimmäisen_pizzan_yksikköhinta > toisen_pizzan_yksikköhinta:
    print(f"Toinen pizza antaa paremman vastineen rahalle. Yksikköhinta: {ensimmäisen_pizzan_yksikköhinta:.2f} €/m²")
else:
    print(f"Molemman pizzat antaa yhtä hyvän vastineen rahalle.{ensimmäisen_pizzan_yksikköhinta:.2f} €/m²")
