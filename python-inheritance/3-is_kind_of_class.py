#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie True si l'objet est exactement une instance
de la classe spécifiée ; sinon False
"""


def is_kind_of_class(obj, a_class):
    """ on retourne la classe spécifié qui est une instance"""
    return isinstance(obj, a_class)
