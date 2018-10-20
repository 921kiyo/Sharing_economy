import os
import sys

from GLOBALS import DATABASE_URL

from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine, Boolean, Float, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(250), nullable=False)
    # email = Column(String(250), nullable=False)
    # picture = Column(String(250))
    donating = Column(Boolean, default=False)
    total_donated = Column(Float, default=0)
    products = relationship("Product")
    # charity_donating = relationship("Charity")

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
    name = Column(String(250), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String(250))
    image = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(250), nullable=False)
    condition = Column(String(10), nullable=False)  #
    size = Column(String(10), nullable=True)
    shipping=Column(Float, default=0)
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

engine = create_engine(DATABASE_URL)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)