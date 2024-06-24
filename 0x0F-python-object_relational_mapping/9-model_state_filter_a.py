#!/usr/bin/python3
"""lists all State objects that contain the letter a """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        user, passwd, host, port, db_name))
    Session = sessionmaker(bind=engine)
    local_session = Session()
    state_a = local_session.query(State).filter(
            State.name.op("regexp")(".*a+.*")).order_by(State.id)
    local_session.close()
    engine.dispose()
    for state in state_a:
        print(f"{state.id}: {state.name}")
