#!/usr/bin/python3
"""
script that prints the State object
 with the name passed as argument from the database hbtn_0e_6_usa
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
    state = s.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    s.close()
