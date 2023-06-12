# Le programme vérifie un tableau initialisé, jusqu'à ce qu'il tombe sur la valeur 9 alors à ce moment là il va vérifier si les 2 numéros font bien 9 en s'additonant, si c'est le cas le programme s'arrête.
j=0
tab= [2,1,3,1,4,1,1,1,1,6,8,4,2]
premier = 0
deuxieme = 0
troisieme = 0
for i in range(len(tab)):
	troisieme=deuxieme
	deuxieme = premier 
	premier = tab[i]
	if troisieme+deuxieme==9 and premier==9:
		j = j+1
print(j)