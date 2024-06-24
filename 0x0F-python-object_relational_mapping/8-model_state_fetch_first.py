#!/usr/bin/python3
"""prints the first state object from the database"""


import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        user, passwd, host, port, db_name, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    local_session = Session()
    first_state = local_session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
