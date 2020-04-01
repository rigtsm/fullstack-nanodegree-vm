# FLASK application

from flask import Flask, render_template

########## Initialize Database CRUD operations ###############
# import for CRUD operations 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# initialize connection to the database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

################################################################


# Anytim we run an application in Python, a special varialble called __name__ gets
# defined for the application and all the import it uses
# 
# The application run by the Python intrepreter gets a name variable set to __name__ = main, whereas all the other
# imported Python files get a __name__ = set to the actial name of the Python file "project"
print("print the name of ", __name__) # __name__ = main

app = Flask(__name__) # instance of the Flask class with the name of the running applications 


# everytime the localhost:5000/ or /hello is visited, the HelloWorld is executed
# the stacking of decorations functions allows me to have multiple link pointing to the sape place (function)
# amazon.com == amazon.com/index
#@app.route('/') # @ decoratior in python
#@app.route('/hello') # Decoratiors essentially wraps our function inside the app.route function
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    ''' From the id at the end of the link, get the menu of that corespinding restaurant'''
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
       
    return render_template('menu.html' , restaurant=restaurant, items = items) 



# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    '''Create route for newMenuItem function here'''
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()

    return "page to create a new menu item for %s . Task 1 complete!" % restaurant.name




# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()

    output = ''
    output += 'From restaurant %s' % restaurant.name
    output += 'edit the menu item %s ' % item.name
    
    return output




# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()

    output = ''
    output += 'From restaurant %s' % restaurant.name
    output += ' delete the menu item %s ' % item.name
    return output
















# make sure the server runs if the script is executed directly from the python interpreter and not used as an 
# imported module
if __name__ == '__main__':
    app.debug = True  ### reload everytime some code is changed, non need for restarting
    app.run(host = '0.0.0.0' , port = 5000 )