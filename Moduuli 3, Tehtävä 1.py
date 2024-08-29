# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla kä
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pi

mitta = float(input("Mikä on kuhan mitta? "))

alamitta = 37 - mitta

if mitta<37:
    print("Laita kuha takaisin järveen, kuha on " + str(alamitta) + " cm alamittainen.")