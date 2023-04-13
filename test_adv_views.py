# test views for waypoints and kudos as well
"""Adventure View tests."""

from app import app, CURR_USER_ID
import os
from unittest import TestCase

from models import db, connect_db, User, Waypoint, Adventure

os.environ['DATABASE_URL'] = "postgresql:///out-there-test"

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class AdventureViewTestCase(TestCase):
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

        self.testadv1 = Adventure(title="My first Adventure!", activity="Hiking", departure_date="07-18-2023", departure_time="07:30",
                                  return_date="07-18-2023", return_time="12:00", notes="It's going to be great!", user_id=self.testuser1.id, location="Asheville, NC")
        self.testadv2 = Adventure(title="My second Adventure!", activity="Swimming", departure_date="07-18-2023", departure_time="07:30",
                                  return_date="07-18-2023", return_time="12:00", notes="It's going to be great!", user_id=self.testuser1.id, location="Asheville, NC")
        db.session.add_all([self.testadv1, self.testadv2])
        db.session.commit()

    def test_show_adventure(self):
        """Should show adventure details."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get(f'/adventures/{self.testadv1.id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(self.testadv1.title, html)

    def test_create_adventure(self):
        """Should create adventure and show details page."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get('/adventures/create')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Create Your Next Adventure', html)

    def test_update_adventure(self):
        """Should update adventure from form data and show new details page."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.get(f'/adventures/{self.testadv1.id}/update')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(self.testadv1.title, html)

    def test_adventures_destroy(self):
        """Should remove adventure from user and redirect to profile."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.post(
                f'/adventures/{self.testadv1.id}/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('My Adventure Log', html)
            self.assertNotIn(self.testadv1.title, html)

    def test_give_kudos(self):
        """Add adv to kudos of user."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            resp = client.post(f'/kudos/{self.testadv1.id}/give')

            self.assertEqual(resp.status_code, 200)
            self.assertIn(self.testadv1, self.testuser1.kudos)

    def test_remove_kudos(self):
        """Remove adv from kudos of user."""

        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_ID] = self.testuser1.id

            self.testuser1.kudos.append(self.testadv1)
            db.session.commit()

            resp = client.post(f'/kudos/{self.testadv1.id}/remove')

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn(self.testadv1, self.testuser1.kudos)

    def test_add_waypoint(self):
        """Adds waypoint to adv"""

    def test_remove_waypoint(self):
        """Removes waypoint from adv"""

    def test_str_locations(self):
        """Generates a contatenated str of all adv waypoints"""

    def test_generate_map(self):
        """Creates a url for mapquest request"""
