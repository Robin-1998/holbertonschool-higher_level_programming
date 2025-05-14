#!/usr/bin/python3
# fonction qui remplace ou ajoute une clé(valeur) dans un dictionnaire

def update_dictionary(a_dictionary, key, value):
    # Met à jour le dictionnaire avec la clé et la valeur fournies
    a_dictionary[key] = value
    # Retourne le dictionnaire mis à jour
    return a_dictionary
