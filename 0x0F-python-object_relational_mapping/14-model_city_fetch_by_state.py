#!/usr/bin/python3

"""Script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session to interact with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    query = session.query(
        State, City).join(City).filter(
        State.id == City.state_id).all()
    for state, city in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
