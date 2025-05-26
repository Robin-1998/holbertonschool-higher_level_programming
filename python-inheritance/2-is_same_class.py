#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie True si l'objet est exactement une instance
de la classe spécifiée ; sinon False
"""

def is_same_class(obj, a_class):
    """ on vérifie si obj est une instance de la class a_class"""
    return type(obj) is a_class
# type(obj) permet de renvoyer la classe exacte de l'objet : obj

