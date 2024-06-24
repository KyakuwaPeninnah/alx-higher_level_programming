#!/usr/bin/python3
"""Script that lists all states"""


from model_state import State, Base
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    db_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
        user, passwd, host, port, db_name)
    engine = create_engine(db_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    states = local_session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    local_session.close()
    engine.dispose()
