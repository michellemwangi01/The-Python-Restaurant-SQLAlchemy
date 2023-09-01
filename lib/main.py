#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # import ipdb; ipdb.set_trace()

