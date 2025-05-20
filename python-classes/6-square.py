#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class qui définit un carré
"""


class Square:
    """ Représente un carré avec une taille donnée. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise une nouvelle instance de Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter pour l'attribut size."""
        return self._size

    @property
    def position(self):
        return self._position

    @size.setter
    def size(self, value):
        """ Setter pour l'attribut size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(v, int) and v >= 0 for v in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """ Calcule l'aire du carré."""
        return self._size * self._size

    def my_print(self):
        """ On imprime le nombde de #"""
        if self.size == 0:
            print()
            return
        for i in range(self._position[1]):
            print()
        for _ in range(self.size):
            print(" " * self._position[0] + "#" * self.size)

# dans le premier for de la fonction my_print on boucle à la deuxième valeur
# de self_position on ajoute un espace

# dans le deuxième for self.size on ajoute " " pour les espaces vides à
# chaque première position et on y ajoute à la suite le nombre de caractère
# spécial dans la boucle
