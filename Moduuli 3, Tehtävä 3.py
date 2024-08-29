# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Sukupuoli? ")
hemoglobiiniarvo = float(input("Hemoglobiiniarvo? [g/l] "))
if sukupuoli == "mies":
    if hemoglobiiniarvo <= 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo >= 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "nainen":
    if hemoglobiiniarvo <= 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarovo >= 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")