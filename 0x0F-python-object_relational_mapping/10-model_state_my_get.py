#!/usr/bin/python3
"""
This module contains a script that lists State objects that
contain 'a' from the database hbtn_0e_6_usa
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

    state = sys.argv[4]
    instance = session.query(State).filter_by(name=state).first()
    if instance:
        print(instance.id)
    else:
        print("Not found")
    session.close()
