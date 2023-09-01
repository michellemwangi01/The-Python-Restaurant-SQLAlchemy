from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///migrations_test.db')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'{self.id}: {self.last_name} {self.first_name})'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    star_rating = Column(Integer())

    def __repr__(self):
        return (f'{self.id}: RestaurantID-{self.restaurant_id} | '
                f'CustomerID-{self.customer_id} | '
                f'Star-rating-{self.star_rating})')



class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f'{self.id}: {self.name} {self.price}.00)'
