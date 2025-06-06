#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui ajoute tous les arguments à une liste python, puis les
enregistre dans un fichier
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args_list = sys.argv[1:]

# récupères les arguments passés en ligne de commande au script, à
# l'exception du nom du script lui-même.
if os.path.exists("add_item.json"):
    liste = load_from_json_file(filename)
else:
    liste = []
liste.extend(args_list)
save_to_json_file(liste, filename)
