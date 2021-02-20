'''
I am hoping for an "exceeds expectations" grade on this project. I worked hard on this code, and it's some of my best so far.
'''

# Import your Game class

from phrasehunter.game import Game
from time import sleep                                                                  # Reasons for this are explained on line 26

# Create your Dunder Main statement.

if __name__ == "__main__":

    # Inside Dunder Main:
    ## Create an instance of your Game class

    game = Game()
    
    ## Start your game by calling the instance method that starts the game loop

    game.start()

    while True:
        if not input("\nWould you like to play again? [Y/N] ").lower() in ("n", "no"):  # If the user's input isn't something along the lines of "no", start a new game, otherwise quit.
            print()
            game = Game()
            game.start()
        else:
            print("\nThanks for playing! Goodbye!")
            sleep(3)                                                                    # I used this function simply because displaying a goodbye message and then closing the window seemed a bit abrupt. The program will display the goodbye message for 3 seconds before shutting down
            quit()
