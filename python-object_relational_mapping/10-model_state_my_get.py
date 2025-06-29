#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui affiche les états (objets) avec le nom passé en argument
"""

import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]

    # Requête sécurisée : filtre exact sur le nom
    state = session.query(State).filter(State.name == state_name).first()

    print(state.id)
