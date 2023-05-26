from random import *
for i in range(11):
	nombre=randrange(0,11)
	calcule = nombre*3
	multiplication = int(input("calcule"+str(nombre)+"x3 ")) # Nombre de ligne important.
	if multiplication == calcule :
		print("C'est juste")
	else : print("C'est faux")
