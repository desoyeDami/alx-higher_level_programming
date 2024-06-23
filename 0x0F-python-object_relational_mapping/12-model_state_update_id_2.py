#!/usr/bin/python3

"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    city_new_name = "New Mexico"

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session to interact with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = city_new_name
        session.commit()
    else:
        print("Not found")
    session.close()
