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
            if self.path.endswith("/hello"):

                self.send_response(200) # successful GET request
                self.send_header('Cntent-type', 'text/html') # inform the client i will reply with a text/html file
                self.end_headers() # send a blank line to indicate the end of the headers response.

                # now lest send some content to the client
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"

                self.wfile.write(output) # Send the message back to the client
                print(output) # just check the output on the console / debuggin porpuse
                return # exit

            # try for url localhost:8080/restaurants
            if self.path.endswith("/restaurants"):

                self.send_response(200) # successful GET request
                self.send_header('Cntent-type', 'text/html') 
                self.end_headers() 

                ## Get le list of the Restorant names and  send some content to the client
                output = ""
                output += "<html><body>"
                output += "<h1> Restaurant List!</h1>"

                restaurants = session.query(Restaurant).all()
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br>"
                output += "</body></html>"

                self.wfile.write(output) # Send the message back to the client
                print(output) 
                return

        except IOError as error:
            print("File not found %s" % self.path)



    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print(output)

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
