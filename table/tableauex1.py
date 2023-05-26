table=[0]*20
compteur = 0
nombre_ascii = ord("a")
while compteur!=20:
	table[compteur] = chr(nombre_ascii+compteur)
	compteur = compteur + 1
print(table)