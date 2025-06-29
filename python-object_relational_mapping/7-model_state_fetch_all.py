#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui liste tout les états (objets) de la database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True
)
# définition
"""
dialect+driver://username:password@host/database
dialect : le type de base de données (ici, mysql)

driver : le pilote utilisé pour se connecter à MySQL (ici, mysqldb)

username : nom d’utilisateur MySQL (donné par sys.argv[1])

password : mot de passe (donné par sys.argv[2])

host : ici localhost, donc le serveur MySQL local

database : nom de la base (donné par sys.argv[3])
"""
session =  sessionmaker(bind=engine)
# On créé notre session via engine, notre base
session = session()
# On créé une connexion temporaire pour exécuter nos oéprations
"""
La session permet d'envoyer des requêtes SQL
on peut supprimer, modifier ou insérer des données

"""
# Requête : récupérer tous les États triés par ID
states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")

