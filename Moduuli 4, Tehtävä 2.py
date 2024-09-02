# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    x_inch = float(input("Anna pituus tuumina: "))
    x_cm = x_inch * 2.54
    print("Annettu tuumapituus on senttimetreinä " + str(x_cm) + " cm.")
    if x_inch < 0:
        break