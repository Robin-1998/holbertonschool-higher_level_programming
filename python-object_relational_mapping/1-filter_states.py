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
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cur = database.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    )

    colonnes = cur.fetchall()

    for colonne in colonnes:
        print(colonne)
