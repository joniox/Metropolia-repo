# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:

    gallonat = float(input("Anna gallonamäärä: "))
    litrat = gallonat_litroiksi(gallonat)
    print("Gallonat on " + str(litrat) + " litraa.")

    if gallonat < 0:
        print("Väärin annettu määrä")
        break