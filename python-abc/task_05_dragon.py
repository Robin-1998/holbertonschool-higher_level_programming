#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe CountedIterator
"""


class SwimMixin:
    """ Class où la créature nage"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """ classe où la créature vole """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ classe où le dragon hérite des deux class cité plus haut"""

    def roar(self):
        print("The dragon roars!")
