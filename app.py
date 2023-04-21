import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
import requests
from flask_cors import CORS

from forms import UserSignUpForm, UserLoginForm, UserUpdateForm, AdventureForm
from models import db, connect_db, User, Adventure, Waypoint, Kudos
from keys import MQ_KEY

CURR_USER_ID = "curr_user"

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///out-there')).replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "16ranchRD")
toolbar = DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)


##########################################################################
# HOMEPAGE & WELCOME PAGE
@app.route('/')
def home_page():
    """
    Show homepage.
    If user is logged in, show the users they are followings' content.
    If not logging in, show welcome page.
    """

    if g.user:
        filtered_ids = [user.id for user in g.user.following] + [g.user.id]
        advs = Adventure.query.filter(
            Adventure.user_id.in_(filtered_ids)).order_by(Adventure.timestamp.desc()).all()
        return render_template("home.html", advs=advs)

    return render_template("welcome.html")


##########################################################################
# USER signup/login/logout
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

    return render_template('users/signup.html', form=form)


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

    return render_template("users/login.html", form=form)


@app.route('/logout')
def logout():
    """Handles user logout."""

    do_logout()
    flash("Successfully logged out. Happy trails!", "success")

    return redirect("/")


##########################################################################
# USER search/show_profile
@app.route('/users')
def search_users():
    """Handles search for users"""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    search = request.args.get('q')

    if not search:
        users = User.query.all()
    else:
        users = User.query.filter(User.username.like(f"%{search}%")).all()

    return render_template('users/search.html', users=users, search=search)


@app.route('/users/<int:user_id>')
def show_profile(user_id):
    """Show user profile with adventures.
    """

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    user = User.query.get_or_404(user_id)

    return render_template('users/profile.html', user=user)


##########################################################################
# USER update/delete
@app.route('/users/update', methods=["POST", "GET"])
def update_user():
    """Handles update profile."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    form = UserUpdateForm(obj=g.user)

    if form.validate_on_submit():
        valid_user = User.authenticate(
            username=g.user.username, password=form.password.data)

        # Check if username has already been taken.
        if form.username.data != g.user.username and User.query.filter_by(username=form.username.data).first() != None:

            flash("Username is already taken.", "danger")
            return render_template('users/update.html', form=form)

        if valid_user:
            user = g.user
            user.username = form.username.data
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.profile_img = form.profile_img.data
            user.bio = form.bio.data
            user.location = form.location.data

            db.session.add(user)
            db.session.commit()
            flash("Profile successfully updated!", "success")
            return redirect(f'/users/{user.id}')

    return render_template('users/update.html', form=form)


@app.route("/user/delete", methods=["POST"])
def delete_user():

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    flash(f"User: {g.user.username} has been deleted.", "success")
    return redirect("/signup")


##########################################################################
# USER Follows Views
@app.route('/users/<int:user_id>/following')
def show_following(user_id):
    """Shows all users user_id is following."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    user = User.query.get_or_404(user_id)

    return render_template('users/following.html', user=user)


@app.route('/users/<int:user_id>/followers')
def show_followers(user_id):
    """Shows all users user_id is followed by."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    user = User.query.get_or_404(user_id)

    return render_template('users/followers.html', user=user)


@app.route('/users/follow/<int:user_id>', methods=["POST"])
def add_follow(user_id):
    """Add user_id to user's following list."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    followed_user = User.query.get_or_404(user_id)
    g.user.following.append(followed_user)
    db.session.commit()

    return jsonify(complete=True)


@app.route('/users/unfollow/<int:user_id>', methods=["POST"])
def remove_follow(user_id):
    """Remove user_id from user's following list."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    followed_user = User.query.get_or_404(user_id)
    g.user.following.remove(followed_user)
    db.session.commit()

    return jsonify(complete=True)

##########################################################################
# ADVENTURE Views


@app.route('/adventures/<int:adv_id>')
def show_adventure(adv_id):
    """Shows details about adventure."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)

    return render_template('adventures/details.html', adv=adv)


@app.route('/adventures/create', methods=["GET", "POST"])
def create_adventure():
    """Handles create adventure and shows form."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    form = AdventureForm()

    if form.validate_on_submit():
        adv = Adventure(title=form.title.data, location=form.location.data,
                        activity=form.activity.data, departure_date=form.departure_date.data, return_date=form.return_date.data, departure_time=form.departure_time.data, return_time=form.return_time.data, notes=form.notes.data, header_img_url=form.header_img_url.data, user_id=g.user.id)
        db.session.commit()
        g.user.adventures.append(adv)
        db.session.commit()

        return redirect(f'/adventures/{adv.id}')

    return render_template('adventures/create.html', form=form)


@app.route('/adventures/<int:adv_id>/update', methods=["GET", "POST"])
def update_adventure(adv_id):
    """Handles create adventure and shows form."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)
    form = AdventureForm(obj=adv)

    if form.validate_on_submit():
        adv.title = form.title.data
        adv.location = form.location.data
        adv.activity = form.activity.data
        adv.departure_date = form.departure_date.data
        adv.return_date = form.return_date.data
        adv.departure_time = form.departure_time.data
        adv.return_time = form.return_time.data
        adv.notes = form.notes.data
        adv.header_img_url = form.header_img_url.data

        db.session.commit()

        return redirect(f'/adventures/{adv.id}')

    return render_template('adventures/update.html', form=form, adv=adv)


@app.route('/adventures/<int:adv_id>/delete', methods=["POST"])
def adventures_destroy(adv_id):
    """Delete an adventure."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get(adv_id)
    db.session.delete(adv)
    db.session.commit()

    return redirect(f"/users/{g.user.id}")

##########################################################################
# Kudos Views


@app.route('/kudos/<int:adv_id>/give', methods=["POST"])
def give_kudos(adv_id):
    """Remove adventure from user's kudos list."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)
    g.user.kudos.append(adv)
    db.session.commit()

    return jsonify(complete=True)


@app.route('/kudos/<int:adv_id>/remove', methods=["POST"])
def remove_kudos(adv_id):
    """Remove adventure from user's kudos list."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)
    g.user.kudos.remove(adv)
    db.session.commit()

    return jsonify(complete=True)

##########################################################################
# Waypoint Views


@app.route('/adventures/<int:adv_id>/waypoint/add', methods=["POST"])
def add_waypoint(adv_id):
    """Add a waypoint to an adventure."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)

    lat = request.json.get('lat')
    long = request.json.get('long')
    color = request.json.get('color')
    name = request.json.get('name')

    wp = Waypoint(lat=float(lat), long=float(long), color=color, name=name)
    db.session.commit()

    adv.waypoints.append(wp)
    db.session.commit()

    return jsonify(id=wp.id)


@app.route('/adventures/waypoint/<int:wp_id>/remove', methods=["POST"])
def remove_waypoint(wp_id):
    """Removes instance of waypoint."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    wp = Waypoint.query.get_or_404(wp_id)
    db.session.delete(wp)
    db.session.commit()

    return jsonify(complete=True)


def str_locations(waypoints):
    """Create a string of waypoints in Mapquest API request format."""

    wp_list = []

    for wp in waypoints:
        location = f"{wp.lat},{wp.long}|via-sm-{wp.color}"
        wp_list.append(location)

    locations = "||".join(wp_list)

    return locations


@app.route('/adventures/<int:adv_id>/map')
def generate_map(adv_id):
    """Create request for Mapquest API and return url."""

    if not g.user:
        flash("Unathorized access. You must be logged in to view.", "danger")
        return redirect("/login")

    adv = Adventure.query.get_or_404(adv_id)

    locations = str_locations(adv.waypoints)

    url = f"https://www.mapquestapi.com/staticmap/v5/map?key={MQ_KEY}&locations={locations}&size=200,200@2x&type=hyb"

    return url
