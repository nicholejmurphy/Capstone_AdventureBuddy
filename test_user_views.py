"""User View tests."""

from app import app, CURR_USER_ID
import os
from unittest import TestCase

from models import db, connect_db, User, Follows, Waypoint, Adventure, AdventuresWaypoints, Kudos

os.environ['DATABASE_URL'] = "postgresql:///out-there-test"

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Waypoint.query.delete()
        Adventure.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="nickmurph", password="user1",
                                    first_name="Nicky", last_name="Murphy")

        db.session.commit()

    def test_home_page(self):
        """Does page show homepage if user is logged in or welcome page if user is not logged in?"""

    def test_login(self):
        """If valid user, does it show home page?"""

    def test_login(self):
        """Should redirect to welcome page?"""

    def test_search_users(self):
        """Should show list of users"""

    def test_show_profile(self):
        """Should show user's profile."""

    def test_update_user(self):
        """Should update user information from form data."""

    def test_delete_user(self):
        """Should remove user and return to welcome page."""

    def test_show_following(self):
        """Should show all users logged in user is following."""

    def test_show_followers(self):
        """Should show all users logged in user is followed by."""

    def test_add_follow(self):
        """Should add user_id to users follow list."""

    def test_remove_follow(self):
        """Should remove user_id to users follow list."""

    def test_show_adventure(self):
        """Should show adventure details."""

    def test_create_adventure(self):
        """Should create adventure and show details page."""

    def test_update_adventure(self):
        """Should update adventure from form data and show new details page."""

    def test_adventures_destroy(self):
        """Should remove adventure from user and rediretc to profile."""

    def test_give_kudos(self):
        """Add adv to kudos of user."""

    def test_remove_kudos(self):
        """Remove adv from kudos of user."""

    def test_add_waypoint(self):
        """Adds waypoint to adv"""

    def test_remove_waypoint(self):
        """Removes waypoint from adv"""

    def test_str_locations(self):
        """Generates a contatenated str of all adv waypoints"""

    def test_generate_map(self):
        """Creates a url for mapquest request"""
