j=0
i=0
tab=[2,6,1,1,1,1,2,4,9,1,1,1,1]
premier = 0
deuxieme = 0
for i in range(len(tab)):
	deuxieme=premier
	premier=tab[i]
	if deuxieme==1 :
		if premier==1:
			j=j+1
print("il y à ",j,"pair de 1")

