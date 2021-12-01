"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    ...
    def __init__(self, dic):
        """
        Reads a file and returns the number of words read
        """
        file = open(dic)
        self.words = self.stripper(file)
        print(len(self.words), " words read")

    # def print_words(self):
    #     file = open(self.dic)
    #     for line in file:
    #         print(line)
    #     file.close()
        
    # def file_len(self,):
    #     with open(self.dic) as f:
    #         for i, l in enumerate(f):
    #             pass
    #     return i + 1

    def stripper(self, file):
        """
        Removes special new-line character
        """
        return [word.strip() for word in file]

    def random(self):
        """
        Returns a random word!
        """
        return choice(self.words)