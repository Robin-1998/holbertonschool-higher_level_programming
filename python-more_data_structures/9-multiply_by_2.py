#!/usr/bin/python3
# fonction qui retourne un nouveau dictionnaire avec les valeurs multiplié par 2

def multiply_by_2(a_dictionary):
    new_dictionnary = {}
    for i in a_dictionary:
        new_dictionnary[i] = a_dictionary[i] * 2
# on ajoute dans le nouveau dictionnaire la valeur du dictionnaire
# de base mais multiplié par 2
    return new_dictionnary
