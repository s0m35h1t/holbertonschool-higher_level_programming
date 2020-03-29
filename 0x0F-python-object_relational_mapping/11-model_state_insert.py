#!/usr/bin/python3
"""
script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
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
    new_state = State(name='Louisiana')
    s.add(new_state)
    state = s.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    s.commit()
    s.close()
