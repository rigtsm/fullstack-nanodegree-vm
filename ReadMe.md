# Flask web server with CRUD operitions on sqlLite local database.

Project based on Udacity web course **Full Stack Foundations**.

Python dependencies: Flask , sqlalchemy .

Start the server:

    python webserver.py

Web page served on localhost:5000.

Change the url to access the other menu Items

    localhost:/restaurants/<int:restaurant_id>

Serving json Api on:

    localhost:/restaurants/<int:restaurant_id>/menu/JSON'
    localhost:/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON'


Database schema