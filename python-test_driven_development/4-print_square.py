#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Fonction qui imprime un carré avec le caractère #
"""
def print_square(size):
    """
    Fonction qui imprime un carré avec le caractère #
    """
    if not isinstance (size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
