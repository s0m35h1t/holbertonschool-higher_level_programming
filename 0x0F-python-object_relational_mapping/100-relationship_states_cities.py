#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    e = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2],
                                                    argv[3])
    engine = create_engine(e)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    cali = State(name="California")
    cali.cities = [City(name="San Francisco")]
    s.add(cali)
    s.commit()
    s.close()
