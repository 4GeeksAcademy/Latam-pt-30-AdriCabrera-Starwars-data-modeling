import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    #Definimos relacion con Favorite
    favorites = relationship("Favorite", back_populates="user")


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite")
    # Relacion con Character
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates="favorite")
    # Relacion con Planet
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates="favorite")
    # Relacion con Species
    species_id = Column(Integer, ForeignKey("species.id"))
    species = relationship("Species", back_populates="favorite")

    

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    # Definimos relacion con Favorite
    favorites = relationship("Favorite", back_populates="character")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    terraine = Column(String(250))
    # Definimos relacion con Favorite
    favorites = relationship("Favorite", back_populates="planet")

class Species(Base):
    __tablename__ = "species"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    language = Column(String(250))
    skin_colors = Column(String(250))
    # Definimos relacion con Favorite
    favorites = relationship("Favorite", back_populates="species")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
