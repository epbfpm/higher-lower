from flask import Flask
from random import randint

app = Flask(__name__)
lives = 6
n = randint(0, 1001)

@app.route('/')
def home():
    return f'<h1>Guess a number between 0 and 1000</h1>' \
           f'<img src="https://media.giphy.com/media/g5qEgeTM20nnO/giphy.gif"></img>'

@app.route('/<n_guess>')
def guess(n_guess):
    n_guess = int(n_guess)
    global lives
    if lives > 1:
        if n_guess > n:
            lives -= 1
            return f'<h1>Too High. Try again. You have {lives} attempts left.</h1>' \
                   f'<img src="https://media.giphy.com/media/SmHXb7cDn1hVoNKZI4/giphy.gif"></img>'
        elif n_guess < n:
            lives -= 1
            return f'<h1>Too low. Try again. You have {lives} attempts left.</h1>' \
                   f'<img src="https://media.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif"></img>'
        elif n_guess == 1:
            return f'<h1>Hori shiiit. You got it!</h1>' \
                   f'<img src="https://media.giphy.com/media/a0h7sAqON67nO/giphy.gif"></img>'
    else:
        return f'<h1>Loser</h1>' \
               f'<img src="https://media.giphy.com/media/26ybwvTX4DTkwst6U/giphy.gif"></img>'


if __name__ == '__main__':
    app.run(debug=True)
