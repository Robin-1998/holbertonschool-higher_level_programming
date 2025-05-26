#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie la liste des attributs et méthodes disponibles d'un objet
"""


def lookup(obj):
    """ retourne la liste des objets """
    return dir(obj)
# la fonction dir affiche tout le contenu d'un objet
