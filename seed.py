from app import db
from models import User, Follows, Adventure, Waypoint, Address

db.drop_all()
db.create_all()

nicky = User.signup(username="nickmurph", password="user1",
                    first_name="Nicky", last_name="Murphy")
danni = User.signup(username="danniHarri$", password="user1",
                    first_name="Danni", last_name="Harris")
chris = User.signup(username="cwcoombs", password="user1",
                    first_name="Chris", last_name="Coombs")
liam = User.signup(username="liamham", password="user1",
                   first_name="Liam", last_name="Harris")
laby = User.signup(username="labycat", password="user1",
                   first_name="Laby", last_name="Moombs")
brett = User.signup(username="brotherbear", password="user1",
                    first_name="Brett", last_name="Harris")

db.session.add_all([nicky, danni, liam, chris, brett, laby])
db.session.commit()

f1 = Follows(user_being_followed_id=1, user_following_id=2)
f2 = Follows(user_being_followed_id=1, user_following_id=3)
f3 = Follows(user_being_followed_id=1, user_following_id=4)
f4 = Follows(user_being_followed_id=1, user_following_id=5)
f5 = Follows(user_being_followed_id=1, user_following_id=6)
f6 = Follows(user_being_followed_id=2, user_following_id=1)
f7 = Follows(user_being_followed_id=3, user_following_id=5)
f8 = Follows(user_being_followed_id=4, user_following_id=3)
f9 = Follows(user_being_followed_id=5, user_following_id=4)
f10 = Follows(user_being_followed_id=6, user_following_id=5)
f11 = Follows(user_being_followed_id=5, user_following_id=6)
f12 = Follows(user_being_followed_id=3, user_following_id=2)
f13 = Follows(user_being_followed_id=4, user_following_id=2)
f14 = Follows(user_being_followed_id=6, user_following_id=2)
f15 = Follows(user_being_followed_id=5, user_following_id=2)


db.session.add_all([f1, f2, f3, f4, f5, f6, f7, f8,
                   f9, f10, f11, f12, f13, f14, f15])
db.session.commit()

a1 = Adventure(title="My first Adventure!", activity="Hiking", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=1, location="Asheville, NC")
a2 = Adventure(title="My first Adventure!", activity="Backpacking", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=2, location="Asheville, NC")
a3 = Adventure(title="My first Adventure!", activity="Swimming", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=3, location="Asheville, NC")
a4 = Adventure(title="My first Adventure!", activity="Mountaineering", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=4, location="Asheville, NC")
a5 = Adventure(title="My first Adventure!", activity="Bushwacking", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=5, location="Asheville, NC")
a6 = Adventure(title="My first Adventure!", activity="Canoeing", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=6, location="Asheville, NC")
a7 = Adventure(title="My second Adventure!", activity="Rafting", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=1, location="Asheville, NC")
a8 = Adventure(title="My second Adventure!", activity="Skiing", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=2, location="Asheville, NC")
a9 = Adventure(title="My second Adventure!", activity="Mountain Biking", departure_datetime="07-18-2023 07:30",
               return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=3, location="Asheville, NC")
a10 = Adventure(title="My second Adventure!", activity="Sledding", departure_datetime="07-18-2023 07:30",
                return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=4, location="Asheville, NC")
a11 = Adventure(title="My second Adventure!", activity="Snowmobiling", departure_datetime="07-18-2023 07:30",
                return_datetime="07-18-2023 12:00", notes="It's going to be great!", user_id=5, location="Asheville, NC")

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11])
db.session.commit()

w1 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w2 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w3 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w4 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w5 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w6 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w7 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w8 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w9 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w10 = Waypoint(lat=35.5950, long=-82.5514, color="blue")
w11 = Waypoint(lat=35.5950, long=-82.5514, color="blue")

db.session.add_all([w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11])
db.session.commit()

a1.waypoints.append(w1)
a2.waypoints.append(w2)
a3.waypoints.append(w3)
a4.waypoints.append(w4)
a5.waypoints.append(w5)
a6.waypoints.append(w6)
a7.waypoints.append(w7)
a8.waypoints.append(w8)
a9.waypoints.append(w9)
a10.waypoints.append(w10)
a11.waypoints.append(w11)

db.session.commit()

address = Address(nickname="Nicky", user_id=1)

db.session.add(address)
db.session.commit()
