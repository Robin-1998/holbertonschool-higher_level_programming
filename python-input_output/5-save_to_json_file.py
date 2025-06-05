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

# la difference entre le dump et le dumps
# dump ecrit directement dans un fichier
# dumps retourne une chaine JSON
