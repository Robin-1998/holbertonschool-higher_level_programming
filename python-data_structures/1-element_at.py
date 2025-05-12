#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    return (my_list[idx])

# Si le return (my_list[idx]) était absent, l’appel element_at(liste, 2)
# n’imprimerait rien (ou None), car la fonction ne renverrait aucune valeur.

