from flask_login import UserMixin
from sqlalchemy import ForeignKey, Text, String, Column, Integer
from sqlalchemy.orm import relationship
from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)

    username = db.Column(String(30), nullable=False, unique=True)
    email = db.Column(String(50), nullable=False, unique=True)
    password = db.Column(String(32), nullable=False)

    posts = relationship("Post", back_populates='author')

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(Integer, primary_key=True, nullable=False)
    user_id = db.Column(ForeignKey('users.id'), nullable=False)

    text = db.Column(Text(600), nullable=False, unique=True)
    title = db.Column(Text(100), nullable=False, unique=True)
    author = relationship("User", back_populates='posts')

    likes = db.Column(Integer, default=0)

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(Integer, primary_key=True, nullable=False)
    user_id = db.Column(ForeignKey('users.id'), nullable=False)
    post_id = db.Column(ForeignKey('posts.id'), nullable=False)
    