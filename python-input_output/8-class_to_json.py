#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie la description du dictionnaire avec une strcuture
de données simple (liste, dictionnaire, chaîne, entier et booléen) pour la
sérialisation JSON d'un objet :
"""


def class_to_json(obj):
    """ on retourne la description du dictionnaire """
    return obj.__dict__

# c'est un attribut spécial contenant un dictionnaire des
# attributs d'instance de l'objet
