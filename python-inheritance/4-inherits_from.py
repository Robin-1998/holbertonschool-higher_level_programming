#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie True si l'objet est une instance d'une class qui a 
hérité(directement ou indirectement) de la classe spécifiée sinon False
"""


def inherits_from(obj, a_class):
    """ si un objet est une instance d’une sous-classe d’une classe donnée"""
    return isinstance(obj, a_class) and type(obj) is not a_class
