#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie un objet (structure de donnée python) représenté par
une chaine JSON
"""
import json


def from_json_string(my_str):
    """ on retourne un objet qui est représenté par une chaine JSON"""
    return json.loads(my_str)
