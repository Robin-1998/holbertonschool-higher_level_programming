#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie True si l'objet est une instance d'une class qui a 
hérité(directement ou indirectement) de la classe spécifiée sinon False
"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class
    args:
        obj: object to check
        a_class: class to check
    returns:
        True or False
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
