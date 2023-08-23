from . import db
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Post(db.Model):

    __tablename__ = 'posts'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(100), unique=True)
    text = Column('text', String(1000))
    date = Column('date', DateTime(timezone=True), default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    likes = Column('likes', db.Integer)
    dislikes = Column('dislikes', db.Integer)

    def __repr__(self):
        return f'ID: {id} | title: {title} | text: {text} | date: {date} | user_id: {id} | likes: {likes} | dislikes: {dislikes}'


class User(db.Model, UserMixin):
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(150), unique=True)
    password = Column('password', db.String(150))
    username = Column('username', db.String(150))
    posts = relationship('Post')