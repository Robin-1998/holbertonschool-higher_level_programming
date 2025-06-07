#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class student qui définit un étudiant avec
"""


class Student:
    """ class étudiant """

    def __init__(self, first_name, last_name, age):
        """ constructeur de la class student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
