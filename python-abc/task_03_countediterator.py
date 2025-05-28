#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe CountedIterator
"""


class CountedIterator:
    """Classe CountedIterator : un itérateur qui compte le nombre 
    d'éléments itérés
    """

    def __init__(self, iteration):
        """
        Constructeur qui initialise l'itérateur à partir d'une séquence 
        iterable et initialise le compteur à zéro.

        :param iteration: un objet itérable (liste, tuple, etc.)
        """
        self.iteration = iter(iteration)
        self.compteur = 0

    def __iter__(self):
        """
        Méthode spéciale qui retourne l'objet itérateur lui-même.
        Cela permet d'utiliser l'objet dans une boucle for.
        """
        return self

    def __next__(self):
        """
        Méthode spéciale pour obtenir l'élément suivant de l'itérateur.
        Incrémente le compteur à chaque appel.

        :return: l'élément suivant de l'itérateur
        :raises StopIteration: si l'itérateur est épuisé
        """
        gondor = next(self.iteration)
        self.compteur += 1
        return gondor

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà itérés.

        :return: le compteur d'éléments consommés
        """
        return self.compteur
