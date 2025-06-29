#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui supprime un état contenant la lettre a
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

    states_to_delete = (
        session.query(State).filter(State.name.like('%a%')).all()
    )

# On sélectionne tous les objets de la table "states"
# On applique un filtre : nom contenant la lettre 'a'
# On exécute la requête et on récupère les résultats sous forme de liste


# On parcourt tous les états trouvés et on supprime celui contenant un 'a'
    for state in states_to_delete:
        session.delete(state)

    # Validation des suppressions dans la base de donnée
    session.commit()
