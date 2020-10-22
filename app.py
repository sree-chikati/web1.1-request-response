# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask #Import the Flask library

app = Flask(__name__) #Set up our app variable so that we can start writing routes.

@app.route('/') 
#@app.route('/'), indicates the URL of the web page we’ll need to visit in order to see our result. In this case, it’s / or the home page
def homepage():
#def homepage():, defines the route function. Whatever this function returns will show up in your browser when you visit the appropriate URL
    """Shows a greeting to the user.""" #docstring, and describes the route in a human-readable way
    return 'Are you there, world? It\'s me, Ducky!' #returns the page contents

if __name__ == '__main__':
    app.run(debug=True)