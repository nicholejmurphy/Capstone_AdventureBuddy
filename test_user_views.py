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

        self.testuser1 = User.signup(
            username="user1", password="user1", first_name="Nicky", last_name="Murphy")
        self.testuser2 = User.signup(
            username="user2", password="user1", first_name="Kyle", last_name="Murphy")

        db.session.commit()

        self.testadv = Adventure(title="My first Adventure!", activity="Hiking", departure_date="07-18-2023", departure_time="07:30",
                                 return_date="07-18-2023", return_time="12:00", notes="It's going to be great!", user_id=self.testuser1.id, location="Asheville, NC")
        self.testwp = Waypoint(lat=35.5950, long=-82.5514,
                               color="blue", name="Basecamp")

        db.session.commit()

        self.testadv.waypoints.append(self.testwp)
        db.session.commit()

    def test_home_page(self):
        """Does page show homepage if user is logged in?"""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Adventure Feed', html)

    def test_login(self):
        """If valid user, does it show home page?"""

        with self.client as client:

            resp = client.get('/login')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Login', html)

    def test_logout(self):
        """If valid user, does it show home page?"""

        with self.client as client:
            resp = client.get('/logout', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Successfully logged out.', html)

    def test_signup(self):
        """Should redirect to welcome page?"""

        with self.client as client:

            resp = client.get('/signup')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('SignUp', html)

    def test_search_users(self):
        """Should show list of users"""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Searched users for', html)

    def test_show_profile(self):
        """Should show user's profile."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get(f'/users/{self.testuser1.id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('My Adventure Log', html)

    # def test_update_user(self):
    #     """Should update user information from form data."""

    # def test_delete_user(self):
    #     """Should remove user and return to welcome page."""

    # def test_show_following(self):
    #     """Should show all users logged in user is following."""

        # with self.client as client:
        #     with client.session_transaction() as session:
        #         session[CURR_USER_ID] = self.testuser1.id

        #     self.testuser1.following.append(self.testuser2)
        #     db.session.commit()

        #     resp = client.get('/')
        #     html = resp.get_data(as_text=True)

        #     self.assertEqual(resp.status_code, 200)
        #     self.assertIn('Adventure Feed', html)

    # def test_show_followers(self):
    #     """Should show all users logged in user is followed by."""

    # def test_add_follow(self):
    #     """Should add user_id to users follow list."""

    # def test_remove_follow(self):
    #     """Should remove user_id to users follow list."""
