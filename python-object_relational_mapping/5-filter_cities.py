#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui prend le nom d'un état en argument et liste toutes les villes
de cet état, en utilisant la base de données hbtn_0e_4_usa
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

# Requête SQL paramétrée (protection contre les injections SQL)
# On sélectionne les noms des villes correspondant à un état donné
    commande = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id;
    """

# Exécution de la requête avec le nom de l'état en argument
    cur.execute(commande, (sys.argv[4],))

# Récupération des résultats et extraction des noms de villes
    cities = [row[0] for row in cur.fetchall()]

# Affichage des noms des villes, séparés par une virgule
    print(", ".join(cities))
