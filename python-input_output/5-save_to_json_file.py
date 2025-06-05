#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui écrit un objet dans un fichier texte, en utilisant une
representation JSON
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)

# la différence entre json dump et json dumps
# json dump écrit directement dans un fichier
# json dumps retourne une chaine JSON
