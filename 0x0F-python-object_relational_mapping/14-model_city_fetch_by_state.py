#!/usr/bin/python3
"""
This module contains a script that lists all
City objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           user, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State.name, City.id,
                                  City.name).filter(
                                  State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
    session.close()
