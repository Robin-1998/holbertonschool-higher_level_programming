#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe CountedIterator
"""


class Fish:
    """ class fish"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """ class bird"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """ class Flyingfish qui hérite de fish et bird """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
