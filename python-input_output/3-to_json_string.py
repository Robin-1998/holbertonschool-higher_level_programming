#!/usr/bin/python3
import json
"""
Projet Holberton
ROBIN D
fonction qui ajoute une chaîne de caracteres a la fin d'un fichier texte
et renvoie le nombre de caracteres ajoutés:
"""


def to_json_string(my_obj):
    """ fonction json"""
    return json.dumps(my_obj)

# json.dumps permet de transformer des objets Python (comme 
# les dictionnaires, listes, etc.) en texte JSON.
