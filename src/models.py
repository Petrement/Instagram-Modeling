#import os
#import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True )
    username = Column(String(50), unique=True, nullable=False )
    first_name = Column(String(50), unique=False, nullable=False )
    last_name = Column(String(50), unique=False, nullable=False )
    email = Column(String(50), unique=True, nullable=False )

class Follower(Base):
    __tablename__="follower"
    id = Column(Integer, primary_key=True )
    user_from_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id"), unique=False, nullable=False)

class Comment(Base): 
    __tablename__="comment"
    id = Column(Integer, primary_key=True )
    comment_text = Column(String(120), unique=False, nullable=True )
    author_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False )
    post_id = Column(Integer, ForeignKey("post.id"), unique=True, nullable=False )

class Post(Base): 
    __tablename__="post"
    id = Column(Integer, primary_key=True )
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

class Media(Base):
    __tablename__="media"
    id = Column(Integer, primary_key=True )
    type = Column(Enum, unique=True, nullable=False)
    url = Column(String(250), unique=True, nullable=False )
    post_id = Column(Integer, ForeignKey("post.id"), unique=True, nullable=False )
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
