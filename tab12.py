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
