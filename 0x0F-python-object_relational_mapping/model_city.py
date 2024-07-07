#!/usr/bin/python3
"""Define City class and create corresponding table in database"""

import sys
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """City class inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

     # Define the relationship to State
    #state = relationship('State', back_populates='City')

if __name__ == "__main__":
    # Connecting to MySQL server running on localhost at port 3306
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database), pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)
