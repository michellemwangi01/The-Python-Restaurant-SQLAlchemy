#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # import ipdb; ipdb.set_trace()

    res1 = session.query(Restaurant).filter(Restaurant.id == 1).first()
    cus2 = session.query(Customer).filter(Customer.id == 2).first()
    rev1 = Review(
        restaurant_id = 1,
        customer_id = 1,
        star_rating = random.randint(1,10)
    )
    print(res1, cus2)
    print(res1.reviews)
    # res1.reviews.append(rev1)
    # session.commit()
    # print(res1.reviews)
    print(cus2.reviews.append(rev1))
    print(session.query(Review).all())




