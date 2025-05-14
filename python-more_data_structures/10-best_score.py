#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, i=a_dictionary.get)

# la fonction max va chercher l'élément le plus grand dans notre dictionnaire
# le .get permet de récupérer la valeur associé à notre clé du dictionnaire
# la valeur est présenté sous le nom de la variable i
