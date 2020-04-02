# Check the jupyter notebook for an interacting example
# populating the database using sqlAlchemy
# https://classroom.udacity.com/courses/ud088/lessons/3621198668/concepts/36123887380923
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import the classes created in the setup file
from database_setup import Base, Restaurant, MenuItem

# with wich database to comunicate 
engine = create_engine('sqlite:///restaurantmenu.db')

# bind the database to the engine class
Base.metadata.bind = engine

# Create a session maker object. Establish a link of communication
# between our code executions and the engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

# Creating a restorant table is equal at creating an object
myFirstRestaurant = Restaurant(name = "Pizza Palace2")
# to persist it in the db i need to perform
session.add(myFirstRestaurant) # not it is in the "stagin zone"
session.commit() # now it is stored at my db

# checking if the commit worked. Applying a query
print(session.query(Restaurant).all())


# adding MenuItem elements
cheesepizza = MenuItem(
	name = "Cheese Pizza"
	, description = "pizza description"
	, course = "Entree"
	, price = "$8.99"
	, restaurant = myFirstRestaurant )













