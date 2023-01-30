tab=[31,28,31,30,31,30,31,30,31]
mois=["Janvier","Février","Mars,","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","decembre"]
for i in range(len(tab)):
	tab3[i*2+1]=tab[i]
	tab3[i*2] = mois[i]
print("tab3")