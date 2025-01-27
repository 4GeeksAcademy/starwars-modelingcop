import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Integer, default=1)

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(10))
    gender = Column(String(20))
    homeworld = Column(String(100))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    rotation_period = Column(String(20))
    orbital_period = Column(String(20))
    diameter = Column(String(20))
    climate = Column(String(20))
    gravity = Column(String(20))
    terrain = Column(String(50))
    surface_water = Column(String(20))
    population = Column(String(20))
    url = Column(String(250))

class BlogPost(Base):
    __tablename__ = 'blog_posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship('User')
    character = relationship('Character')

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship('User')
    planet = relationship('Planet')

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('blog_posts.id'))
    user = relationship('User')
    blog_post = relationship('BlogPost')

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')