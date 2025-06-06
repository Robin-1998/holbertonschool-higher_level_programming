#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class student qui définit un étudiant avec 
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ constructeur de la class student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ récupère une représentation du dict d'une instance d'étudiant """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}

# Si attrs est une liste de noms d'attributs,
# retourne seulement les attributs listés (et existants).

# résumé pour le return de fin :
# Pour chaque élément attr dans la liste attrs, si l'objet self a un
# attribut nommé attr, alors ajoute dans un nouveau dictionnaire :
# la clé = attr et la valeur = la valeur de cet attribut.
