"""SQLAlchemy models for Warbler."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

DEFAULT_PROFILE_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Windows_10_Default_Profile_Picture.svg/512px-Windows_10_Default_Profile_Picture.svg.png?20221210150350"
DEFAULT_ADV_HEADER = "https://images.unsplash.com/photo-1524959888614-3ab5712bf527?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80"


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
    profile_img = db.Column(db.Text, default=DEFAULT_PROFILE_IMG)
    bio = db.Column(db.Text, default="Here for an adventure!")
    location = db.Column(db.Text, default="OutThere somewhere...")

    # User Relationships
    adventures = db.relationship("Adventure", backref="user")
    addresses = db.relationship("Address", backref="user")
    kudos = db.relationship(
        "Adventure", secondary="kudos", backref="kudos")
    followers = db.relationship("User", secondary="follows", primaryjoin=(
        Follows.user_following_id == id), secondaryjoin=(Follows.user_being_followed_id == id))
    following = db.relationship("User", secondary="follows", primaryjoin=(
        Follows.user_being_followed_id == id), secondaryjoin=(Follows.user_following_id == id), overlaps="followers")

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
    def signup(cls, username, first_name, last_name, password):
        """Creates a hashed password and adds user to database."""
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
        user = User(username=username, first_name=first_name,
                    last_name=last_name, password=hashed_pwd)
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


class Adventure(db.Model):
    """An adventure from a user."""

    __tablename__ = 'adventures'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    title = db.Column(
        db.String(100),
        nullable=False,
    )
    location = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    activity = db.Column(db.Text, nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    return_date = db.Column(db.Date, nullable=False)
    return_time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.Text, default="No notes yet.")
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )
    header_img_url = db.Column(db.Text, default=DEFAULT_ADV_HEADER)

    # Adventure Relationships
    waypoints = db.relationship(
        "Waypoint", secondary="adventures_waypoints", backref="adventure")


class Waypoint(db.Model):
    """Waypoints associated with an adventure."""

    __tablename__ = "waypoints"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    color = db.Column(db.String, nullable=False, default="red")
    name = db.Column(db.String, nullable=True)


class AdventuresWaypoints(db.Model):
    """A collection of relationships between adventures and waypoints."""

    __tablename__ = "adventures_waypoints"

    adventure_id = db.Column(db.Integer, db.ForeignKey(
        'adventures.id', ondelete='cascade'), primary_key=True)
    waypoint_id = db.Column(db.Integer, db.ForeignKey(
        'waypoints.id', ondelete='cascade'), primary_key=True)


class Kudos(db.Model):
    """Kudos between Users and Adventures"""

    __tablename__ = "kudos"

    adventure_id = db.Column(db.Integer, db.ForeignKey(
        'adventures.id', ondelete='cascade'), primary_key=True)
    kudos_from_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), primary_key=True)


class Address(db.Model):
    """Contacts for each user."""

    __tablename__ = "addresses"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    nickname = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False, default=+19898176328)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )


def connect_db(app):
    """Connetcs database to app.py"""

    db.app = app
    db.init_app(app)
