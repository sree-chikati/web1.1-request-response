# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

#TUTORIAL 1: HELLO WORLD!
from flask import Flask #Import the Flask library

app = Flask(__name__) #Set up our app variable so that we can start writing routes.

@app.route('/') 
#@app.route('/'), indicates the URL of the web page we’ll need to visit in order to see our result. In this case, it’s / or the home page
def homepage():
#def homepage():, defines the route function. Whatever this function returns will show up in your browser when you visit the appropriate URL
    """Shows a greeting to the user.""" #docstring, and describes the route in a human-readable way
    return 'Are you there, world? It\'s me, Ducky!' #returns the page contents



#REQUIRED 1: YOUR FAVORITE ANIMAL
@app.route('/penguins')
def penguins_page():
    return "Penguins are cute!"

@app.route('/dogs')
def dogs_page():
    return "Dogs are adorable!"


#TUTORIAL 1: YOUR USER'S FAVORITE ANIMAL
@app.route('/animal/<users_animal>')
#indicates the URL of the web page we’ll need to visit. 
#The angle brackets, < and >, denote a route variable for which the user can type anything at all! 
#The value of whatever the user types into the URL will be available in a variable called users_animal
def favorite_animal(users_animal): #takes in the variable users_animal
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!' #returns the result



if __name__ == '__main__':
    app.run(debug=True)