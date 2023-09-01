from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref

from main import Base
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
