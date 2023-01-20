from random import * 
position = 0
nbr_carte= 0
while nbr_carte==3:
	carte = randrange(1,11)
	position = position + 1
	if carte //2 ==0:
		nbr_carte=nbr_carte + 1
		print("Carte = "carte)
		
if position < 5:
	print("La carte était dans les 4 premières cartes.")
else :
	print("La carte était plus loin dans la liste.")

			
 	 