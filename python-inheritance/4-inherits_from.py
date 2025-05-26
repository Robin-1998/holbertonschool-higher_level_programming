#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
fonction qui renvoie True si l'objet est une instance d'une class qui a 
hérité(directement ou indirectement) de la classe spécifiée sinon False
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a subclass (direct or indirect)
    of the specified class. Return False otherwise.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True 
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
