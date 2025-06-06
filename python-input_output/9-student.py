#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class student
"""


class Student:
    """ constructeur de la class student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method qui récupère une représentation du 
        dictionnaire d'une instance d'étudiant """
        return self.__dict__
