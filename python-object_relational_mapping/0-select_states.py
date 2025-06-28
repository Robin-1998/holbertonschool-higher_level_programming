#!/usr/bin/ python3
"""
Projet Holberton
ROBIN D
Script qui liste tout les états de la database hbtn_0e_0_usa
"""
# Importation du module MySQLdb pour interagir avec une base MySQL
import MySQLdb
from sys import argv
# Importation de argv pour récupérer les arguments passés en ligne de commande

if __name__ == "__main__":
# Cette condition vérifie que le script est exécuté directement 
# (pas importé dans un autre script)

# Connexion à la base de données MySQL
# Les paramètres de connexion sont récupérés dans argv :
# argv[1] = nom d'utilisateur MySQL (ex: 'holberton')
# argv[2] = mot de passe de l'utilisateur
# argv[3] = nom de la base de données (ex: 'hbtn_0e_0_usa')
    db = MySQLdb.connect(
        host="localhost",
# Adresse du serveur MySQL (ici la machine locale)
        port=3306,
# Port MySQL par défaut
        user=argv[1],
# Utilisateur MySQL passé en argument
        passwd=argv[2],
# Mot de passe passé en argument
        db=argv[3]
# Nom de la base de données passée en argument
    )
    
    cur = db.cursor()
# Création d'un curseur qui sert à exécuter des requêtes SQL

# Exécution de la requête SQL qui sélectionne toutes les colonnes 
# de la table 'states',
# triées par l'id dans l'ordre croissant
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
# cur.execute() renvoie le nombre de lignes retournées par la requête

# On parcourt toutes les lignes obtenues, une par une, grâce au nombre de lignes
    for i in range(num_rows):

# cur.fetchone() récupère la ligne suivante du résultat sous forme de tuple,
# ici (id, nom_de_l'état)

        print(cur.fetchone())  # Affiche la ligne récupérée

