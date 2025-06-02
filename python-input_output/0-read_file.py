#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui lit un fichier texte et l'imprime sur stdout
"""


def read_file(filename=""):
    """ fonction lecture de fichier """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
