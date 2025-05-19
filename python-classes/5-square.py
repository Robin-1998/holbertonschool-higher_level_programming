#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class qui définit un carré
"""


class Square:
    """ Représente un carré avec une taille donnée. """

    def __init__(self, size=0):
        """ Initialise une nouvelle instance de Square."""
        self.size = size

    @property
    def size(self):
        """ Getter pour l'attribut size."""
        return self._size

    @size.setter
    def size(self, value):
        """ Setter pour l'attribut size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """ Calcule l'aire du carré."""
        return self._size * self._size

    def my_print(self):
        """ On imprime le nombde de #"""
        for i in range(self._size):
            print(self._size * '#')
        if self.size == 0:
            print()
