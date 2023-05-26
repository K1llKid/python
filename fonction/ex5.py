# définir une fonction sur fCercle(r). 
# Cette fonction doit retourner la surface (l'aire) 
# d'un cercle dont on lui a fourni le 
# rayon r en argument.
# Par exemple l'éxécution 
# de l'instruction print(surf Cerle(2.5)) 
# doit donner le résultat 19.635 rappel : pi.r² 
# et la valeur précise py se trouve dans le module Math.

# pi (variable from math import pour pi)

from math import *

def Cercle(rayon):
	surface = pi*rayon**2
	return surface
print(Cercle(2.5))

# ATTENTION, si fonction retourner une valeur (utiliser return)

