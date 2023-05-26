# Définir une fonction volBoite(x1,x2,x3) 
# qui retourne le volume d'une boite parallélépipédique 
# ont on fournit les trois dimensions x1,x2,x3
 # en arguments.

# Par exemple l'exécution de l'instruction, 
# print(volBoite(5.2, 7.7, 3.3)) doit donner le résultat :
# 132.13
def volBoite(x1,x2,x3):
	air=x1*x2*x3 
	return air
print(volBoite(5.2,7.7,3.3))