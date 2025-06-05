#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui retourne la representation Json d'un objet (chaine)
"""
import json


def to_json_string(my_obj):
    """ return the JSON representation"""
    return json.dumps(my_obj)

# json dumpss permet de transformer des objets Python (comme
# les dictionnaires, listes, etc.) en texte JSON.
