# Using the BaseHttpServer library
# I will be using python3 so i will use someting different
#from http.server import BaseHTTPRequestHandler, HTTPServer # not working

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # Works perfectly for python 2

# The server is devided in two main sections
######### handler section ######### 
# Here we indicate what code to execute based on the type of HTTP request that is sent to the server

class webserverHandler(BaseHTTPRequestHandler):

    # handle the GET request our server receives and shold figure out which resources are requeste to access
    def do_GET(self):
        try:
            
            if self.path.endswith("/hello"):

                self.send_response(200) # successful GET request
                self.send_header('Cntent-type', 'text/html') # inform the client i will reply with a text/html file
                self.end_headers() # send a blank line to indicate the end of the headers response.

                # now lest send some content to the client
                output = ""
                output += "<html><body>Hello Bro!</body></html>"
                self.wfile.write(output) # Send the message back to the client
                print(output) # just check the output on the console / debuggin porpuse
                return # exit

        except IOError as error:
            print("File not found %s" % self.path)


######### main section #########
# We instantiate our server and specify what port it will listen to
def main():
    try:
        # specify the port
        port = 8080
        
        # instantiate the server: HttpServer( serveraddress , RequestHandlerClass)
        server = HTTPServer(('', 8080) , webserverHandler)

        print("Web server is running on port %s" % port)

        # keep the server constantely listening
        server.serve_forever()

    except KeyboardInterrupt as error: # CTRL + c typed by the user
        print("  CTRL + c typed by the user. Stoping web server...")
        server.socket.close()





# run immediatly the main method when the interpreter executes the script
if __name__ == '__main__':
    main()