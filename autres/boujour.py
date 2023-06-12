position = 0
tab =["yo","salut","oui","hi","hallo","bonjour","hola","yamete","sus","aurevoir","bye","gyuc","fsdf"]
for i in range(len(tab)) :
        
	if "bonjour" == tab[i]:
		position = i+1
        
if position <=5:
	print("Bonjour se trouvait dans les 5 premier")
elif position <=10:
	print("Bonjour se trouvait dans les 5 suivants")
else :
	print("Bonjour se trouvait plus loin")
