#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui affiche les états (objets) avec le nom passé en argument
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Création d'une nouvelle instance de State
    new_state = State(name="Louisiana")

    # Ajout dans la session
    session.add(new_state)

    # Validation dans la base
    session.commit()

    # Affichage de l'ID de l'état ajouté
    print(new_state.id)
