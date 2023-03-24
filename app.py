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


##########################################################################
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


def do_logout():

    if CURR_USER_ID in session:
        del session[CURR_USER_ID]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle signup."""

    form = UserSignUpForm()

    if form.validate_on_submit():
        try:
            user = User.signup(username=form.username.data, first_name=form.first_name.data,
                               last_name=form.last_name.data, password=form.password.data)
            db.session.commit()
        except IntegrityError:
            flash("Username is already taken.", "danger")
            return render_template('users/signup.html', form=form)

        do_login(user)
        return redirect('/')

    return render_template('user/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user  login."""

    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            do_login(user)
            flash(f"Welcome {user.first_name}!", "success")
            return redirect('/')

        flash("Invalid username or password.", "danger")

    return render_template("templates/users/login.html", form=form)


@app.route('/logout')
def logout():
    """Handles user logout."""

    do_logout()
    flash("Successfully logget out. Happy trails!", "success")

    return redirect("/")
