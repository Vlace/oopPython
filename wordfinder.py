"""Word Finder: finds random words from a dictionary."""
import random



class WordFinder:
    def __init__(self, txt_doc):
        self.file1 = self.word_list(txt_doc)
        print(len(self.word_list(txt_doc)), 'words read')
    def word_list(self, txt_doc):
        file = open(txt_doc)
        lines = file.readlines()
        return lines
    def random(self):
        return random.choice(self.file1).strip()

class SpecialWordFinder(WordFinder):
    def random(self):
        self.word_returned = random.choice(self.file1).strip()
        if self.word_returned.strip() and not self.word_returned.startswith('#'):
            return self.word_returned

