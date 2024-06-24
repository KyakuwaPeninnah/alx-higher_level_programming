#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    state = local_session.query(State).filter(
                            State.name.like(state_name)).first()
    if state:
        print(state.id)
    else:
        print("Not found")
        local_session.close()
        engine.dispose()
