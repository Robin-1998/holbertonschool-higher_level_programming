#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe abstraite : Shape
"""


class VerboseList(list):
    def append(self, item):
        """ mathod qui ajoute un élément à la fin de la liste """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """ method qui ajoute des éléments de liste spécifiés à la fin
            de la liste actuelle
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """ method qui supprime un élément spécifié d'une liste """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=-1):
        """ method qui supprime l'élément à la position spécifiée """
        boromir = super().pop(item)
        print(f"Popped [{boromir}] from the list.")

# on utilise -1 car on appelle sans argument, exemple pop(), ça enlève
# le dernier élément et si tu appels pop(0), ça enlève le premier, etc
