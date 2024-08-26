# 1 leiviskä on 20 naulaa
# 1 naula on 32 luotia
# 1 luoti on 13,3 grammaa

leiviskät = float(input("Anna leiviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

luodit_grammoina = luodit * 13.3
naulat_grammoina = naulat * 13.3 * 32
leiviskät_grammoina = leiviskät * 13.3 * 32 * 20

g_konversio_summa = luodit_grammoina + naulat_grammoina + leiviskät_grammoina

kg, g = divmod(g_konversio_summa / 1000, 1)

print(f"Massa nykymittojen mukaan on {kg} kilogrammaa ja {g * 1000:6.2f} grammaa.")




