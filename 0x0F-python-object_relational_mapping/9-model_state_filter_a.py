#!/usr/bin/python3
"""
This module contains a script that lists the first
State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
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

    for instance in session.query(State).filter(
            State.name.ilike('%a%')).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.close()
