from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

'''----------------------------------- R E T A U R A N T -------------------------------------------'''


class Restaurant(Base):
    # define Restaurant table name
    __tablename__ = 'restaurants'

    # create class attributes and table columns
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # create class relationships as attributes
    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer')

    # represent the class instances
    def __repr__(self):
        return f'{self.name} Restaurant - Price: ${self.price}.00\n'

    # return details of all the restaurant instance reviews
    def all_reviews(self):
        return [
            f'Review for {self.name} by {session.query(Customer).filter(Customer.id == review.customer_id).first().full_name}: {review.star_rating}stars.'
            for review in self.reviews]


    # return all the restaurant instance reviews
    @property
    def restaurant_reviews(self):
        return self.reviews

    # return all the customers who have reviewed this restaurant
    @property
    def restaurant_customers(self):
        return self.customers

    # returns the fanciest(most-expensive) restaurant of all the restaurants
    @classmethod
    def fanciest_restaurant(cls):
        all_restaurants = session.query(cls).all()
        return f'The fanciest restaurant is {max(all_restaurants, key=lambda restaurant: restaurant.price)}.'


'''------------------------------------ C U S T O M E R ---------------------------------------------'''


class Customer(Base):
    # define Restaurant table name
    __tablename__ = 'customers'

    # create class attributes and table columns
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # create class relationships as attributes
    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant')

    # represent the class instances
    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}\n'

    # returns the customer reviews
    @property
    def customer_reviews(self):
        return self.reviews

    # returns the customer reviews
    @property
    def customer_restaurants(self):
        return self.restaurants

    # return customer full_name
    @property
    def full_name(self):
        return f'{self.last_name},{self.first_name}'

    # return restaurant with the highest review for this customer
    def favorite_restaurant(self):
        best_rated = max(self.reviews, key=lambda review: review.star_rating)
        restaurantid = best_rated.restaurant_id
        return f'{self.full_name}\'s favorite restaurant(s) is {[restaurant for restaurant in self.restaurants if restaurant.id == restaurantid][0]}.'

    # add review and return it
    def add_review(self, restaurant, rating, description):
        new_review = Review(
            restaurant_id=restaurant.id,
            customer_id=self.id,
            star_rating=rating,
            description=description,
        )
        session.add(new_review)
        session.commit()
        # session.refresh(new_review)
        return new_review

    # delete reviews that belong to specific restaurants
    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter(Review.restaurant_id == restaurant.id,
                                                         Review.customer_id == self.id)
        reviews_to_delete.delete()
        session.commit()
        print(f'{self.first_name}\'s reviews for \'{restaurant.name} restaurant\' have been successfully deleted!')


'''----------------------------------- R E V I E W ------------------------------------------------'''


class Review(Base):
    # create Review table name
    __tablename__ = 'reviews'

    # create class attributes and table columns
    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    description = Column(String())
    star_rating = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    # create class relationships as attributes
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    # represent the class instances
    def __repr__(self):
        return (f"Customer({self.customer_id}) | Restaurant({self.restaurant_id}) | start-rating({self.star_rating}) |"
                f" {self.description}: {self.star_rating} stars\n")

    # return customer
    @property
    def review_customer(self):
        return self.customer

    # return customer
    @property
    def review_restaurant(self):
        return self.restaurant

    # return full review details
    def full_review(self):
        return f"Review for '{self.restaurant.name} restaurant' by '{self.customer.full_name}': {self.star_rating} stars\n"
