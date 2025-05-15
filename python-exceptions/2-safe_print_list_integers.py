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
        except (ValueError, IndexError):
            pass  # on sort de la liste après
    print()
    return compteur
