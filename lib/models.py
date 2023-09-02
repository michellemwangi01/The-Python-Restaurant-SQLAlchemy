from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///restaurants.db')

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    description = Column(String())
    star_rating = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))


    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    def __repr__(self):
        return (f'{self.id}: RestaurantID-{self.restaurant_id} | '
                f'CustomerID-{self.customer_id} | '
                f'Star-rating-{self.star_rating})')

    def review_customer(self):
        return self.customer


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant')

    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name})'


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer')

    def __repr__(self):
        return f'{self.id}: {self.name} {self.price}.00)'
