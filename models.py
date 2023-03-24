"""SQLAlchemy models for Warbler."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class Follows(db.Model):

    __tablename__ = "follows"

    user_being_followed_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), primary_key=True)
    user_following_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), primary_key=True)

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)
    profile_img = db.Column(db.Text, default='images/default_profile_img.png')
    bio = db.Column(db.Text)
    location = db.Column(db.Text)

    # User Methods
    following = db.relationship("User", secondary="follows", primaryjoin=(Follows.user_following_id == id), secondaryjoin=(Follows.user_being_followed_id == id) )
    followers = db.relationship("User", secondary="follows", primaryjoin=(Follows.user_being_followed_id == id), secondaryjoin=(Follows.user_following_id == id) )





