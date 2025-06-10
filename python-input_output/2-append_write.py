#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui ajoute une chaîne de caracteres a la fin d'un fichier texte
et renvoie le nombre de caracteres ajoutés:
"""


def append_write(filename="", text=""):
    """ imprime le nombre de caractère dans la chaîne de caractère """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))

        
