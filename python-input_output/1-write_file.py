#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui imprime une chaîne de caractère dans un fichier texte et
retourne le nombre de caractère écrit
"""


def write_file(filename="", text=""):
    """ imprime le nombre de caractère dans la chaîne de caractère """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))

# le 'w' est un mode d'ouverture du fichier, et il signifie write
# permet d'écrire dans le fichier
