#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class My_list qui hérite de list
"""


class MyList(list):
    """
    MyList est en héritage par rapport à list
    """

    def print_sorted(self):
        """ imprime la liste dans l'ordre croissant"""
        print(sorted(self))
