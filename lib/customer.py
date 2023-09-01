from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from main import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
