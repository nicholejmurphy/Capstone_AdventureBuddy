"""SQLAlchemy models for Warbler."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class Follows(db.Model):
    """Tracks reltionships of users following users."""

    __tablename__ = "follows"

    user_being_followed_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), primary_key=True)
    user_following_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), primary_key=True)


class User(db.Model):
    """Represents users in system."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)
    profile_img = db.Column(db.Text, default='images/default_profile_img.png')
    bio = db.Column(db.Text)
    location = db.Column(db.Text)

    # User Relationships
    following = db.relationship("User", secondary="follows", primaryjoin=(
        Follows.user_following_id == id), secondaryjoin=(Follows.user_being_followed_id == id))
    followers = db.relationship("User", secondary="follows", primaryjoin=(
        Follows.user_being_followed_id == id), secondaryjoin=(Follows.user_following_id == id))

    # User Instance Methods
    def _repr_(self):
        """Makes representation of user in returns readable."""

        return f"<User #{self.id}: {self.username}"

    def is_followed_by(self, other_user):
        """If user is followed by other_user, return True, else - return False."""

        found_follower = [
            user for user in self.followers if user == other_user]
        return len(found_follower) == 1

    def is_following(self, other_user):
        """If user is follwoing other_user, return True - else, return False."""

        found_in_following = [
            user for user in self.following if user == other_user]
        return len(found_in_following) == 1

    # User Classmethods
    @classmethod
    def signup(cls, username, first_name, last_name, password, profile_img):
        """Creates a hashed password and adds user to database."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
        user = User(username=username, first_name=first_name,
                    last_name=last_name, password=password, profile_img=profile_img)

        db.session.add(user)

        return user

    @classmethod
    def authenticate(cls, username, password):
        """If user is found, returns user - else, returns False."""

        user = cls.query.filter_by(username=username).first()

        if user:
            authorized = bcrypt.check_password_hash(user.password, password)
            if authorized:
                return user

        return False


def connect_db(app):
    """Connetcs database to app.py"""

    db.app = app
    db.init_app(app)
