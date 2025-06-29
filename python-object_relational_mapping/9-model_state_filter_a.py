#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui liste tout les états contenant une lettra 'a'
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

    states_with_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
    )

    # Affichage
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
