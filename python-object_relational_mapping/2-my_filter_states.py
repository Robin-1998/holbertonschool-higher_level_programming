#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui prend un argument et affiche toutes les valeurs de la table des
états de hbtn_0e_0_usa dont le nom correspond à l'argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                .format(sys.argv[4]))
    # Affichage  ligne par ligne
    for state in cur.fetchall():
        print(state)
