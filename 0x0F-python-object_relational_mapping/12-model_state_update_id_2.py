#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
  sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker()
session = Session(bind=engine)

new_name = session.query(State).filter(State.id == 2).first()
new_name.name = "New Mexico"
session.commit()
