import sys
# this part regards the configuration
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

# Create an instance of the Base class just imported, special classes that corespond
# to tables in the database
Base = declarative_base()


# the class code is the object-oriented rapresentation of a table in the db
# We will create two classes coresponding to the two tables of our database
class Restaurant(Base):
    
    # rapresentation of a table inside the class
    __tablename__ = 'restaurant'

    # Mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)





class MenuItem(Base):
    # rapresentation of a table inside the class
    __tablename__ = 'menu_item'

    # Mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(80))
    restaurant_id = Column( Integer , ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



######### Insert at the end fo the file #############
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
