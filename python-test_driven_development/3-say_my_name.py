#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Fonction qui imprime my name is premier_nom et deuxième_nom
"""


def say_my_name(first_name, last_name=""):
    """
        Write a function that prints My name is <first_na> <last_na>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
