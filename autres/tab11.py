# Pas besoin d'initaliser le i car c'est compris dans le tableau.
# La variable -> deuxieme n'a pas besoin d'être initialisée au début.

# Enoncé adapté : En lancant un programme dans un tableau avec des nombres entiers quand il tombe sur 0 il continue et après il signalera combien de fois il à eu de paire de 1 successifs.
j=0
tab=[2,6,1,1,1,1,2,4,9,1,1,1,1]
premier = 0
for i in range(len(tab)):
	deuxieme=premier
	premier=tab[i]
	if deuxieme==1 and premier==1: # Au lieu d'utiliser un IF imbriqué on peut utiliser l'opérateur and.
			j=j+1
print("il y à ",j,"paire.s de 1")

