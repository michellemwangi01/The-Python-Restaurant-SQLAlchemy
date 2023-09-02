from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()
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
        return f'Restaurant({self.restaurant_id}) | Customer({self.customer_id}) | Star-rating({self.star_rating}) | {self.description}\n'

    @property
    def review_customer(self):
        return self.customer

    @property
    def review_restaurant(self):
        return self.restaurant


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant')

    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}\n'

    @property
    def customer_reviews(self):
        return self.reviews

    @property
    def customer_restaurants(self):
        return self.restaurants

    @property
    def full_name(self):
        return f'{self.last_name},{self.first_name}'

    @property
    def fanciest_restaurant(self):
        max_price = max([restaurant.price for restaurant in self.restaurants])
        return max_price

    @property
    def favorite_restaurant(self):
        best_rated = max(self.reviews, key=lambda review: review.star_rating)
        restaurantid = best_rated.restaurant_id
        fave_restaurant = [restaurant for restaurant in self.restaurants if restaurant.id == restaurantid]
        return fave_restaurant

    def add_review(self, restaurant, rating, description):
        new_review = Review(
            restaurant_id = restaurant.id,
            customer_id = self.id,
            star_rating = rating,
            description = description,
        )
        session.add(new_review)
        session.commit()
        # session.refresh(new_review)
        return new_review

    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter(Review.restaurant_id == restaurant.id, Review.customer_id == self.id)
        print(reviews_to_delete.all())
        reviews_to_delete.delete()
        session.commit()
        print(f'{self.first_name}\'s reviews for \'{restaurant.name} restaurant\' have been successfully deleted!')


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer')

    def __repr__(self):
        return f'{self.name} Restaurant - Price: ${self.price}.00)\n'

    @property
    def restaurant_reviews(self):
        return self.reviews

    @property
    def restaurant_customers(self):
        return self.customers
