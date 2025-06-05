#!/usr/bin/python3
import json
"""
Projet Holberton
ROBIN D
fonction qui retourne la representation Json d'un objet (chaine)
"""


def to_json_string(my_obj):
    """ fonction json"""
    return json.dumps(my_obj)

# json dumpss permet de transformer des objets Python (comme
# les dictionnaires, listes, etc.) en texte JSON.
