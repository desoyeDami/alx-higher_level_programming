#!/usr/bin/python3

"""Script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session to interact with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    letter = "a"
    states = session.query(State).filter(State.name.like(f'%{letter}%')).all()
    for state in states:
        session.delete(state)
        session.commit()

    session.close()
