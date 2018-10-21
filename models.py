import os
import sys

from GLOBALS import DATABASE_URL

from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine, Boolean, Float, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    sex = Column(String(1), nullable=False)  # M / F
    country = Column(String(25), nullable=False)
    city = Column(String(25), nullable=False)
    age = Column(Integer, nullable=False)
    haversine_distance = Column(Float, default=0)
    donating = Column(Boolean, default=False)
    total_donated = Column(Float(precision=2), default=0)
    monthly_donations = Column(Float(precision=2), default=0)
    products = relationship("Product")
    charity_id = Column(Integer, nullable=True)

    @property
    def serialize(self):
      return{
          "id": self.id,
          "name": self.name,
          "donating": self.donating,
          "total_donated": self.total_donated
          # 'email': self.email,
          # 'picture': self.picture
      }


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String(250))
    image = Column(String(250), nullable=False)
    price = Column(Float(precision=2), nullable=False)
    condition = Column(String(10), nullable=False)  #
    size = Column(String(10), nullable=True)
    shipping = Column(Float(precision=2), default=0)
    sold = Column(Boolean, default=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "description": self.description,
            "price": self.price
        }


class Charity(Base):
    __tablename__ = 'charity'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    mission = Column(String(500), nullable=False)
    url = Column(String(100), nullable=True)
    media = Column(String(100), nullable=True)
    amount_raised = Column(Float(precision=2), default=0)
    num_donators = Column(Integer, default=0)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mission": self.mission,
            "url": self.url,
            "amount_raised": self.amount_raised,
            "num_donators": self.num_donators,
        }


engine = create_engine(DATABASE_URL)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)