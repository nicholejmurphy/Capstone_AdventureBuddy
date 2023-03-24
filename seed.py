from app import db
from models import User, Follows

db.drop_all()
db.create_all()

nicky = User(username="nickmurph", password="user1",
             first_name="Nicky", last_name="Murphy")
danni = User(username="danniHarri$", password="user1",
             first_name="Danni", last_name="Harris")
chris = User(username="cwcoombs", password="user1",
             first_name="Chris", last_name="Coombs")
liam = User(username="liamham", password="user1",
            first_name="Liam", last_name="Harris")
laby = User(username="labycat", password="user1",
            first_name="Laby", last_name="Moombs")
brett = User(username="brotherbear", password="user1",
             first_name="Brett", last_name="Harris")

db.session.add_all([nicky, danni, liam, chris, brett, laby])
db.session.commit()

a = Follows(user_being_followed_id=1, user_following_id=2)
b = Follows(user_being_followed_id=1, user_following_id=3)
c = Follows(user_being_followed_id=1, user_following_id=4)
d = Follows(user_being_followed_id=1, user_following_id=5)
e = Follows(user_being_followed_id=1, user_following_id=6)
f = Follows(user_being_followed_id=2, user_following_id=1)
g = Follows(user_being_followed_id=3, user_following_id=5)
h = Follows(user_being_followed_id=4, user_following_id=3)
i = Follows(user_being_followed_id=5, user_following_id=4)
j = Follows(user_being_followed_id=6, user_following_id=5)
k = Follows(user_being_followed_id=5, user_following_id=6)
l = Follows(user_being_followed_id=3, user_following_id=2)
m = Follows(user_being_followed_id=4, user_following_id=2)
n = Follows(user_being_followed_id=6, user_following_id=2)
o = Follows(user_being_followed_id=5, user_following_id=2)

db.session.add_all([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o])
db.session.commit()
