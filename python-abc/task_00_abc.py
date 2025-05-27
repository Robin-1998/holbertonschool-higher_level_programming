#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe abstraite : Animal
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Class principale """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """ Sous-classe chien """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """ Sous-classe chat """

    def sound(self):
        return "Meow"
