import os

from flask import Flask, render_template, request, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserSignUpForm, UserLoginForm, UserUpdateForm
from models import db, connect_db, User

CURR_USER_ID = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///out-there'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "16ranchRD")
toolbar = DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)

# User signup/login/logout


@app.before_request
def add_user_to_global():
    """If user is logged in, add to Flask Global"""

    if CURR_USER_ID in session:
        g.user = User.query.get(session[CURR_USER_ID])

    else:
        g.user = None


def do_login(user):
    """Log user in."""

    session[CURR_USER_ID] = user.id


def do_logout(user):

    if CURR_USER_ID in session:
        del session[CURR_USER_ID]


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user  login."""
