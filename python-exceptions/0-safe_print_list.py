#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # compteur va servir à compter combien d'éléments on a réussi à imprimer
    compteur = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            compteur += 1
        except IndexError:
            break  # on sort de la liste après
    print()
    return compteur

# On essaie d'accéder à l'élément my_list[i]
# Si l’élément existe, on l’imprime sans aller à la ligne
# "{}".format(...) sert juste à afficher proprement n’importe quel type
# Et pour finir, on retourne combien d’éléments on a réellement imprimés
