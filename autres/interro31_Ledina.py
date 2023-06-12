from random import * 
position = 0
nbrcarte= 0
carte = randrange(1,11)
print("Carte = ",carte)
while nbrcarte==3:
	carte = randrange(1,11)
	print("Carte = ",carte)
	position = position + 1
	if carte //2 ==0:
		carte = valeur
		nbrcarte=nbrcarte + 1
		print("Carte = ",carte)
if position < 5:
	print("La carte était dans les 4 premières cartes.")
else :
	print("La carte était plus loin dans la liste.")

			

