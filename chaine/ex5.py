tab=str("Ecrivez une phrase")
compteur=0
for i in range(len(tab)):
	if tab[i] == "":
		compteur = compteur + 1
	else : 
		tab2 = tab2+tab[i]
question = int(input("Combien de mots y à t'il?"))
if question==compteur:
	print("Félicitation vous avez trouvés !")
else :
	print("La réponse était ",compteur)
	