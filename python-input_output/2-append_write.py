#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui ajoute une chaîne de caractères à la fun d'un fichier texte 
(UTF8) et renvoie le nombre de caractères ajoutés:
"""


def append_write(filename="", text=""):
    """ imprime le nombre de caractère dans la chaîne de caractère """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
