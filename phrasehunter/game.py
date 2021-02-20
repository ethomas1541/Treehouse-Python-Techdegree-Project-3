'''
I am hoping for "exceeds expectations" on this project. See app.py
'''

# Create your Game class logic in here.

from .phrase import Phrase              # Phrase is imported into and used by game.py
from random import choice as choose     # Used to take random phrases

class Game:
    def __init__(self):     # Init method that initializes all the requested attributes, which are all used later
        self.missed = 0
        self.phrases = (
            "Take me out to the ball game",
            "We gonna rock down to electric avenue",
            "Medium rare steak please",
            "Please keep your hands and feet inside the vehicle at all times",
            "We live on the most boring street in the country"
        )
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        print("Welcome to Phrase Hunters! Good luck!\n")

    def get_random_phrase(self):        # Sets the phrase that will be used in this particular game
        return choose(self.phrases)

    def get_guess(self):
        while True:
            guess = input("\nGuess a letter: ").upper()     # Guesses must be stored as uppercase, otherwise phrase.display won't work correctly, for reasons explained in that module. The game runs perfectly as long as they are stored as uppercase
            if guess.isalpha() and len(guess) == 1:         # Logic for checking if the guess is a single letter, i.e. is alphabetical and 1 in length
                return guess
                break
            else:
                print("\nPlease type a single letter!")     # This will print indefinitely until the input function recieves an ideal input. In my case, I chose not to penalize the player for incorrectly formatted guesses

    def game_over(self, won: bool):     # A boolean is passed to this method that denotes whether the player won or lost
        if won:
            print("\nCongratulations! You guessed the phrase!")
        else:
            print("\nYou ran out of lives! Better luck next time!")
    
    def start(self):
        self.active_phrase = self.get_random_phrase()   # Choose a phrase to use throughout the game
        phrase = Phrase(self.active_phrase)             # Pass that phrase to a new instance of the Phrase class
        print("Welcome to Phrase Hunter! When prompted, guess a letter. 5 incorrect guesses and the game will end!\n")
        while True:
            phrase.display(self.guesses)    # Always display the phrase first, updated with the user's guesses
            if phrase.check_complete():     # If phrase.hidden_phrase has been updated and now matches the phrase chosen by the game, the player has won. Pass True to game_over and break the main loop
                self.game_over(True)
                break
            elif self.missed > 4:           # If the user has made more than 4 incorrect guesses, we know they've lost. Pass False to game_over and break the main loop
                self.game_over(False)
                break
            guess = self.get_guess()        # If the player hasn't won or lost yet, we know they're still in the middle of a game. Take their guess
            if phrase.check_letter(guess):  # If the letter is present in the phrase (be it uppercase or lowercase), add it to the list of guesses, thus ensuring the next call of phrase.display when the loop repeats will be up-to-date
                self.guesses += guess
            else:                           # Otherwise, the player has guessed incorrectly. add 1 to their misses and print a warning message, like so:
                self.missed += 1
                print(f"\nYou have {5 - self.missed} out of 5 lives remaining!")
            print()                         # Make some whitespace, simply for formatting purposes
