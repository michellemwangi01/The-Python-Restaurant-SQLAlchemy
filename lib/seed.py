from faker import  Faker
import random


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Customer).delete()
    session.query(Review).delete()
    session.query(Restaurant).delete()

    fake = Faker()

    customers = []
    for i in range(10):
        customer = Customer(
            first_name=fake.name(),
            last_name=fake.name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.unique.name(),
            price=random.randint(4000,10000)
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)


    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,3)):
            customer = random.choice(customers)
            review = Review(
                restaurant_id=restaurant.id,
                description=fake.sentence(),
                star_rating=random.randint(1, 10),
                customer_id=customer.id


            )
            if restaurant not in customer.restaurants:
                customer.reviews.append(review)
                session.commit()

    session.close()


