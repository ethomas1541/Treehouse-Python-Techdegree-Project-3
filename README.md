# Treehouse-Python-Techdegree-Project-3
These files contain a fully functioning "Phrase Hunter" game, traditionally known as "Hangman".

Three files are used: app.py, game.py and phrase.py.
  
  - app.py is simply an "entry point" where an instance of the Game class from game.py is created and thus the game begins. After the user finishes their game, they may choose to play again, which will overwrite their current instance with a new instance of the Game class, or quit the game, which will close the console after 3 seconds.
  - game.py contains all the actual behavior of the game. It imports and makes extensive use of the Phrase class from phrase.py. The game's behavior happens in Game.start, which almost entirely consists of method calls to either Game or Phrase.
  - phrase.py handles the bulk of the game's background processes, such as checking whether the user has won, checking if their guess is correct or incorrect, and most importantly, using a list of the user's guessed letters to update its own hidden_phrase attribute, which is the spaces-and-underscores the user sees when the game starts, and the basis of any guesses they make.
