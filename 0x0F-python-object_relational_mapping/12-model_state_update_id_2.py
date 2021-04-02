#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '___main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
      sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadate.create_all(engine)

    session = Session(engine)

    new_name = session.query(State).filter(State.id == 2).one()
    new_name.name = "New Mexico"
    session.commit()
    session.close()
