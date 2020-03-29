#!/usr/bin/python3
"""
Write a script that lists all State objects
from the database hbtn_0e_6_usa
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    e = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2],
                                                    argv[3])
    engine = create_engine(e)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    for state in s.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    s.close()
