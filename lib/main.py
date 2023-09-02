#!/usr/bin/env python3

import random
from sqlalchemy.orm import sessionmaker

from models import *

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # import ipdb; ipdb.set_trace()

    res5 = session.query(Restaurant).filter(Restaurant.id == 5).first()
    cus2 = session.query(Customer).filter(Customer.id == 2).first()
    rev1 = Review(
        restaurant_id = 1,
        customer_id = 1,
        star_rating = random.randint(1,10),
        description = "regret is for fools! I praise my mistakes, coz they led me to you!"
    )
    print(rev1)
    # print(res1, cus2)
    # print(res1.reviews)
    # res5.reviews.append(rev1)
    # session.commit()
    # print(res1.reviews)
    # print(cus2.reviews.append(rev1))
    # print(session.query(Review).all())

    # print(rev1.review_customer())
    # print(rev1.restaurant())


    res5 = session.query(Restaurant).filter(Restaurant.id == 5).first()
    # print(res5.restaurant_reviews)
    # print(res5.restaurant_reviews())

    # cus10 = session.query(Customer).filter(Customer.id == 10).first()
    # print(cus10)
    # print(cus10.customer_reviews())
    # restaurants = cus10.favorite_restaurant
    # print(restaurants)

    # print(cus10.add_review(restaurant=res5, rating=8, description="country music"))
    # cus10.delete_reviews(res5)
    # print(cus10.customer_reviews)

    # print(Restaurant.fanciest_restaurant())

    print(res5.all_reviews())












