#!/usr/bin/python3
"""Write a script that changes the name of a State object
from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql
password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
Your code should not be executed when imported"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format
        (user, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"

    session.commit()

    session.close()
