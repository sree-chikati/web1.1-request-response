# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

#TUTORIAL 1: HELLO WORLD!
from flask import Flask #Import the Flask library
import random #For STRETCH CHALLANGE 4

app = Flask(__name__) #Set up our app variable so that we can start writing routes.

@app.route('/') 
#@app.route('/'), indicates the URL of the web page we’ll need to visit in order to see our result. In this case, it’s / or the home page
def homepage():
#def homepage():, defines the route function. Whatever this function returns will show up in your browser when you visit the appropriate URL
    """Shows a greeting to the user.""" #docstring, and describes the route in a human-readable way
    return 'Are you there, world? It\'s me, Ducky!' #returns the page contents



# ------------------------------------------- REQUIRED CHALLANGES ------------------------------------------------

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


#REQUIRED 2: YOUR USER'S FAVORITE DESSERT
@app.route('/dessert/<users_dessert>')
def fav_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'


#REQUIRED 3: MAD LIBS
@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f' Is that {adjective} cake for {noun}? They will be super happy!'


#REQUIRED 4: MULTIPLY 2 NUMBERS
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        ans = int(number1) * int(number2)
        return f'{number1} times {number2} is {ans}.'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'



# ------------------------------------------- STRETCH CHALLANGES --------------------------------------------------

#STRETCH CHALLANGE 1: SAY N TIMES
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit():
        answer = ""
        for i in range(int(n)):
            answer += word + " "
            print(answer)
        return answer
    else:
         return f'Invalid input. Please try again by entering a word and a number!'
    

#STRETCH CHALLANGE 2: REVERSE A STRING
    #HINT: Use a for loop to loop over each character in the string, 
    #starting at the end; add each one to a result string as you go.
@app.route('/reverse/<word>')
def reverse(word):
    switch = ""
    for i in word:
        switch = i + switch
    return switch


#STRETCH CHALLANGE 3: STRANGE CAPS
@app.route('/strangecaps/<word>')
def strangecaps(word):
    new = ''
    for i, value in enumerate(word): 
    #For i and value in enumerate( which is a method that adds a counter to word)
        if i % 2 == 0:
        # if i index in word is divided by 2 and returns a 0 remainder, lowercase the letter in that index
            new += value.lower()
        else:
        # else when i index in the word is divided by 2 and doesn't return a 0 remainder, uppercase the letter
            new += value.upper()
    return new


#STRETCH CHALLANGE 4: DICE GAME
@app.route('/dicegame')
def dicegame():
    diceroll = random.randint(1,6)
    if diceroll != 6:
        return f"You rolled a {str(diceroll)}. You lost!"
    else:
        return f"You rolled a {str(diceroll)}. You won!"

   
if __name__ == '__main__':
    app.run(debug=True)