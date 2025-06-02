#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui lit un fichier texte et l'imprime sur stdout
"""


def read_file(filename=""):
    """ fonction lecture de fichier """
    with open('my_file_o.txt', encoding="utf-8") as f:
        filename = f.read()

    f.closed
True
