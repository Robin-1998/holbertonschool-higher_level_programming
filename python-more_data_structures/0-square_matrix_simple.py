#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    grand_stock = []
    for i in matrix:
        stock = []
        for j in i:
            stock.append(j * j)  # on multiplie toute nos valeur
        grand_stock.append(stock)  # on les intègre dans notre grand tableau
# vu que c'est un tableau en 2 dimensions
    return stock


# les [] permet de stocker les lignes de la grande matrice qui contient
# les racines carrés
# la 2ème est une ligne temporaire
