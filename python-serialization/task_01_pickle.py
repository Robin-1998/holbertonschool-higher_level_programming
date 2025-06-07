#!/usr/bin/python3
""" fonction de sérialisation et déséralisation d'un fichier JSOn """
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        """ constructeur de l'objet"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method prints out attributes"""
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Charge un objet CustomObject"""
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        return obj
