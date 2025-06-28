#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui liste tout les états dont le nom commence par un N majuscule
dans la base de donnée
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host ="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cur = database.cursor()

    num_rows = cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    )
# WHERE name LIKE 'N%' va garder que les noms d'états qui commencent par N
# on peut quand même continuer en y rajoutant le trie par identifiant
    colonnes = cur.fetchall()

# Fetchall va réucpérer de son côté tout les colonnes qui correspondent

    for colonne in colonnes:
        print(colonnes)


