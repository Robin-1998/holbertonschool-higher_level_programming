#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return (my_list[idx])

# Si le return était absent, l’appel element_at(liste, 2) par exemple
# n’imprimerait rien (ou None), car la fonction ne renverrait aucune valeur.

