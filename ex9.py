def nomMois(n):
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    if n >= 1 and n <= 12:
        return mois[n - 1]
    else:
        return "Mois invalide"

print(nomMois(2))


# Dans le code corrigé, l'indice n - 1 est utilisé pour accéder à l'élément correspondant dans la liste mois.

# En Python (et dans de nombreux autres langages de programmation), les indices des listes commencent à partir de zéro. Cela signifie que le premier élément de la liste a un indice de 0, le deuxième élément a un indice de 1, et ainsi de suite.

# Dans notre cas, les mois sont stockés dans la liste mois, où l'indice 0 correspond à "Janvier", l'indice 1 correspond à "Février", l'indice 2 correspond à "Mars", et ainsi de suite jusqu'à l'indice 11, qui correspond à "Décembre".

# Lorsque vous appelez la fonction nomMois(n) et que vous passez un numéro de mois n, nous voulons renvoyer le nom du mois correspondant. Par exemple, si vous appelez nomMois(2), nous voulons renvoyer "Février".

# Cependant, puisque les indices commencent à partir de zéro, nous devons ajuster le numéro de mois n en le réduisant de 1 pour obtenir l'indice correct dans la liste. Par conséquent, nous accédons à l'élément mois[n - 1] pour obtenir le nom du mois correspondant.

# En résumé, l'indice n - 1 est utilisé pour ajuster le numéro du mois de manière à correspondre à l'indice correct dans la liste des mois. Cela permet d'accéder au nom du mois correspondant dans la liste mois.