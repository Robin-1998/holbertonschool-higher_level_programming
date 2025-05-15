#!/usr/bin/python3
# fonction qui imprime les x premiers éléments de la liste et
# seulement les entiers
def safe_print_list_integers(my_list=[], x=0):
    # on initialise notre compteur pour parcourir ta boucle
    compteur = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            compteur += 1
        except (ValueError, TypeError):
            # on gère le cas de valeur erronée dans un type de données
            # spécifié + apparaît lorsque deux types différents sont combinés
            pass  # on passe à la liste suivante
    print()
    return compteur
