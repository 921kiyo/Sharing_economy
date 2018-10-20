import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
      return{
          'name': self.name,
          'email': self.email,
          'picture': self.picture
      }

class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
      return{
          'name': self.name,
          'id': self.id
      }

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    # date = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)

    @property
    def serialize(self):
      return{
          'title': self.title,
          'body': self.body,
          'id': self.id
      }

engine = create_engine('sqlite:///genrearticlewithusers.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)