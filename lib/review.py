from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from main import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurant.id'))
    review_id = Column(Integer(), ForeignKey('review.id'))
    star_rating = Column(Integer())
