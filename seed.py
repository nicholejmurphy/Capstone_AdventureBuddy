from app import db
from models import User, Follows


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
