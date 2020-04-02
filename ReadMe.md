# Flask web server with CRUD operitions on sqlLite local database.

Project based on Udacity web course [Full Stack Foundations](https://github.com/udacity/Full-Stack-Foundations).

Python dependencies: Flask , sqlalchemy .

Start the server:
    
    # initialize db
    python database_setup.py
    
    # populate db
    populating_db.py
    
    # start the server
    python webserver.py

Web page served on localhost:5000.

Change the url to access the other menu Items

    localhost:/restaurants/<int:restaurant_id>

Serving json Api on:

    localhost:/restaurants/<int:restaurant_id>/menu/JSON'
    localhost:/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON'


Database schema created with database_setup.py
![db schema](https://github.com/rigtsm/fullstack-nanodegree-vm/blob/master/restaurantdb.png)
