#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Fonction qui divise tout les éléments de la matrice
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError(
            " matrix must be a matrix (list of lists) of integers/floats")
    if not len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int or float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix

# ligne 16 - Elle permet de construire une nouvelle matrice,
# où chaque élément est :
# le résultat de la division de l’ancien élément x par div
# arrondi à 2 décimales
