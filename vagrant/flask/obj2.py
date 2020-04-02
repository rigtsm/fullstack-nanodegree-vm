# FLASK application

from flask import Flask, render_template, request, redirect, url_for

# library render_template for passing and doing for loops on the varialbles
# library request : enabling GET POST requests

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
@app.route('/')
def homeRoute():
    return redirect(url_for('restaurantMenu', restaurant_id = 1))


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id = 2):
    ''' From the id at the end of the link, get the menu of that corespinding restaurant'''
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    print(">>>>>>>>>>>>>",type(items))
    # pass the variables to be visualized directly on the html
    return render_template('menu.html' , restaurant=restaurant, items = items) 



# Task 1: Create route for newMenuItem function here
# Adding Get Post
@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    '''Create route for newMenuItem function here. Handle the GET and POST request to the server'''
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    
    if request.method == 'POST':
        
        newItem = MenuItem( 
            name = request.form['name']
            ,restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()

        # rederecting the user to previos page
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    
    else: # received a GET request. Reply with the web page with the form for the item 
        
        restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
        #return "Get request from the client. \n Page to create a new menu item for %s ." % restaurant.name
        return render_template('newmenuitem.html', restaurant_id = restaurant_id , restaurant=restaurant)



@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    
    # Request after the user entered a new Name for the menu item 
    if request.method == 'POST':
        if request.form['name'] : # if i insert a different name
            item.name = request.form['name']
            
        session.add(item)
        session.commit()

        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    
    return render_template('editmenuitem.html'
        , restaurant_id = restaurant_id 
        , menu_id = menu_id
        , restaurant=restaurant
        , item = item)

    

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()

    if request.method == 'POST':

        session.delete(item)
        session.commit()

        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id)) 

    return render_template('deletemenuitem.html'
            , restaurant_id = restaurant_id 
            , menu_id = menu_id
            , restaurant=restaurant
            , item = item)
















# make sure the server runs if the script is executed directly from the python interpreter and not used as an 
# imported module
if __name__ == '__main__':
    app.debug = True  ### reload everytime some code is changed, non need for restarting
    app.run(host = '0.0.0.0' , port = 5000 )