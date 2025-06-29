#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui affiche le premier état (object) de la database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()


# Requête SQLAlchemy pour récupérer le premier état (State) par ordre
# croissant d'ID
# 1. session.query(State) => sélectionne tous les objets de la table 'states'
# 2. .order_by(State.id) => trie les résultats par ID (croissant)
# 3. .first() => renvoie seulement le premier résultat (ou None si vide)
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
