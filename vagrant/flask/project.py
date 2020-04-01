# FLASK application

from flask import Flask

# Anytim we run an application in Python, a special varialble called __name__ gets
# defined for the application and all the import it uses
# 
# The application run by the Python intrepreter gets a name variable set to __name__ = main, whereas all the other
# imported Python files get a __name__ = set to the actial name of the Python file "project"
print("print the name of ",__name__) # __name__ = main

app = Flask(__name__) # instance of the Flask class with the name of the running applications 


# everytime the localhost:5000/ or /hello is visited, the HelloWorld is executed
@app.route('/') # @ decoratior in python
@app.route('/hello') # Decoratiors essentially wraps our function inside the app.route function
def HelloWorld():
    return "Hello Fuckin World wi Flask"


# make sure the server runs if the script is executed directly from the python interpreter and not used as an 
# imported module
if __name__ == '__main__':
    app.debug = True  ### reload everytime some code is changed, non need for restarting
    app.run(host = '0.0.0.0' , port = 5000 )