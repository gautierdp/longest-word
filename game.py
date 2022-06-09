import string
import random

class Game:
    """_summary_
    Creates a validator for Scrabble cheaters
    """
    def __init__(self):
        """_summary_
        retrieves choice
        """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """_summary_
        checks if word is valid
        Args:
            word (_type_): random word with random letters

        Returns:
            _type_: bool
        """
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
