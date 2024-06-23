#!/usr/bin/python3
"""Define State class and create corresponding table in database"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connecting to MySQL server running on localhost at port 3306
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)
