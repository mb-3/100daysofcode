from flask import Flask
import random
import time

## This game is a Flask approach to the Higher Lower game from an ealier day. 
## Personally, I think this is a poor design as this does not take in user input in a friendly way. (Typing "/" then a number in the url isn't a fun game)

app = Flask(__name__)

correct_num = random.randint(0, 9)


@app.route("/")
def home_screen():
    return f'<h1>Guess a number between 0 and 9: </h1>' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_check(guess):
    if guess > correct_num:
        return f'<h1>Too high! Try again.</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < correct_num:
        return f'<h1>Too low! Try again. </h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1>You got it! </h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

# Debug off
if __name__ == "__main__":
    app.run()
