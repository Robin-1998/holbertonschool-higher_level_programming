#!/usr/bin/python3
def search_replace(my_list, search, replace):
    grand_stock = []
    for i in my_list:
        if i == search:
            grand_stock.append(replace)
        else:
            grand_stock.append(i)
    return grand_stock
