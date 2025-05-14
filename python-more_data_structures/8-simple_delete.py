#!/usr/bin/python3
# fonction qui supprime une clé du dictionnaire

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
