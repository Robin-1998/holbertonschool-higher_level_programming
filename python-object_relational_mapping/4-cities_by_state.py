#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui liste toutes les villes de la database hbtn_0e_4_usa
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

    commande = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(commande)
    rows = cur.fetchall()

    for row in rows:
        print(row)
