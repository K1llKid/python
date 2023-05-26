jour = ["lundi","mardi","mercredi",1800,20.357,"jeudi","vendredi"]
print(jour[2])
print(jour[4])
jour[3]=jour[3] + 47
print(jour)
jour[3] = "juillet"
print(jour)
print(len(jour))
del(jour[4])
print(jour)
semaine = jour
print(semaine)
compteur=0
jour[2] = semaine[compteur + 3]
print(jour)
print(semaine)