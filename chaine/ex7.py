x=0
chaine=input("Entrer un mot")
x=len(chaine)
for i in range(len(chaine)):
	if chaine[i] == chaine[len(chaine)-1-i]:
		x=x+1
if x==len(chaine):
	print(chaine,"est correcte")