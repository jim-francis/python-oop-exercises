"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    Reads and returns a word from a file.
    """
    ...
    def __init__(self, dic):
        """
        Reads a file and returns the number of words read
        """
        file = open(dic)
        self.words = self.stripper(file)
        print(len(self.words), " words read")

    def search(self, file):
        """
        Removes special new-line character
        """
        return [word.strip() for word in file]

    def random(self):
        """
        Returns a random word!
        """
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    Reads and return a word from a file, excluding words that start with #
    """
    def search(self, file):
        """
        Searches for a word in a file and returns the word. Excludes words starting with #
        """
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]