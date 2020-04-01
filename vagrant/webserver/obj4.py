####################################
# 2. Add  links in restaurants webpage in the way do edit or delete a restaurant entry.
##############################################

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # Works perfectly for python 2
import cgi

########## Initialize Database CRUD operations ###############
# import CRUD operations 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
###################################################




class webServerHandler(BaseHTTPRequestHandler):

    # handle the GET request our server receives and shold figure out which resources are requeste to access
    def do_GET(self):
        try:
            
            # try for url localhost:8080/restaurants
            if self.path.endswith("/restaurants"):

                # get the list of the restaurants
                restaurants = session.query(Restaurant).all()

                # Create a link to open a new page restaurants/new
                output = ""
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"

                self.send_response(200) # successful GET request
                self.send_header('Cntent-type', 'text/html') 
                self.end_headers() 
                
                output += "<html><body>"
                output += "<h2> Restaurant List!</h2>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # Objective 2 -- Add Edit and Delete Links
                    #output += "<a href ='#' > Edit </a> "
                    # Objective 4 , Add edit web page
                    output += "<a href = '/restaurants/%s/edit' > Edit </a> " % restaurant.id
                    output += "</br>"
                    output += "<a href =' #'> Delete </a>"
                    output += "</br></br></br>"

                output += "</body></html>"

                self.wfile.write(output) # Send the message back to the client
                return


            if self.path.endswith("/restaurants/new"):

                self.send_response(200) 
                self.send_header('Cntent-type', 'text/html') 
                self.end_headers()

                # now lest send back some content to the client
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant!</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"

                self.wfile.write(output) # Send the message back to the client
                return
            

            if self.path.endswith("/edit"):

                # get the id of the restaurant from link "/restaurants/id/edit"
                restaurantIdPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIdPath).one()

                if myRestaurantQuery != []:

                    self.send_response(200) 
                    self.send_header('Cntent-type', 'text/html') 
                    self.end_headers()

                    # now lest send back some content to the client
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Update %s 's name!!!</h1>" % myRestaurantQuery.name
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/%s/edit'>" % restaurantIdPath
                    output += "<input name = 'newRestaurantName' type = 'text' placeholder = %s > " % myRestaurantQuery.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form></body></html>"

                    self.wfile.write(output) # Send the message back to the client
                    return

            
        except IOError as error:
            print("File not found %s" % self.path)



    def do_POST(self):
        try:

            if self.path.endswith("/edit"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    # extract the information from the form 
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # get the item to update the name
                    restaurantIdPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIdPath).one()

                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()


            if self.path.endswith("/restaurants/new"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    # extract the information from the form 
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # create and ad the new item
                    newRestaurant = Restaurant( name = messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
            
            

        except:
            pass






######### main section #########
# We instantiate our server and specify what port it will listen to
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web Server running on port %s" % port )
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()



# run immediatly the main method when the interpreter executes the script
if __name__ == '__main__':
    main()
