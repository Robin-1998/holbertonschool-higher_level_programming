#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    grand_stock = []
    for i in matrix:
        stock = []
        for j in i:
            stock.append(j * j)
        grand_stock.append(stock)
    return grand_stock

# ligne 7: on multiplie toute nos valeur
# ligne 8 : on les intègre dans notre grand tableau vu
# ligne 8 : que c'est un tableau en 2 dimensions

# les [] permet de stocker les lignes de la grande matrice qui contient
# les racines carrés
# la 2ème est une ligne temporaire
