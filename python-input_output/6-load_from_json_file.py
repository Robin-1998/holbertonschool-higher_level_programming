#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui créé un objet à partir d'un fichier JSON
"""
import json


def load_from_json_file(filename):
    """ création d'un objet à partir d'un fichier JSON"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
