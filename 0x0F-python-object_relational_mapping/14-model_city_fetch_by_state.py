#!/usr/bin/python3
"""
script that prints all City objects
from the database hbtn_0e_14_usa:
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    e = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2],
                                                    argv[3])
    engine = create_engine(e)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    rows = s.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    s.close()
