'''
I am hoping for "exceeds expectations" on this project. See app.py
'''

# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase: str):
        self.phrase = phrase                # phrase is the phrase given my game.start, and is the "answer" the user is trying to guess.
        self.hidden_phrase = ''             # hidden_phrase is the most important variable in the game. It's printed every time the main loop runs, and updates whenever the user guesses correctly
        for char in self.phrase:            # This loop simply fills up hidden_phrase with spaces and underscores, wherever appropriate based on the shape of the true phrase
            if char == " ":
                self.hidden_phrase += (" ")
            else:
                self.hidden_phrase += ("_")

    def display(self, update_chars: list):                      # This method both updates and prints out the hidden_phrase attribute, taking into account the user's guesses
        self.hidden_phrase = ''                                 # hidden_phrase must be emptied out so that the updated version isn't simply added on top of the existing version
        for phrase_char in self.phrase:
            uppercase = phrase_char.isupper()                   # Find out whether or not the character in question is uppercase. This will preserve the case of the letter, but not force the user to guess both cases of a single letter.
            if phrase_char.upper() in update_chars:             # If the letter in question is one the user has guessed, make sure it shows up in the updated hidden_phrase, in its original case. My usage of phrase_char.upper() is the reason why user guesses must be taken and stored as uppercase, but this doesn't impair the game in any way.
                if uppercase:
                    self.hidden_phrase += phrase_char.upper()
                else:
                    self.hidden_phrase += phrase_char
            elif phrase_char == " ":                            # If the given character isn't actually in the phrase, simply re-iterate the loop in the initializer; add spaces and underscores wherever needed.
                self.hidden_phrase += " "
            else:
                self.hidden_phrase += "_"

        print(self.hidden_phrase)                               # Print out the updated hidden_phrase attribute, with the user's guesses added to it
        
    def check_letter(self, letter: str):                # Returns True if the given letter is present in the phrase in any way
        return letter.upper() in self.phrase.upper()
        
    def check_complete(self):                           # Returns True if the hidden_phrase attribute has been updated enough to match the original phrase, in which case the user has won.
        return self.hidden_phrase == self.phrase
        
