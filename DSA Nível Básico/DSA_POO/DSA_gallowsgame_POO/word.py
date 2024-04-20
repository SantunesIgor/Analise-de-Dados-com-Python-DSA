import random, re

class Word():
    def __init__(self, word):
        self.word = random.choice(word)
        self.wordscreen = ['_' for _ in self.word]
        self.stages = 0
        self.letterlist = []
        self.code = 0

    def letter(self, letter):
        if letter [:1] == letter and letter in re.findall(r'[a-z]', letter):
            self.code = 0
            if letter in self.letterlist: self.code = 2
            else: 
                self.letterlist.append(letter)
                if letter in self.word: self.wordscreen = [k if k == letter else v for k, v in (zip(self.word, self.wordscreen))]
                else: 
                    if self.stages != 6: self.stages += 1
        else: self.code = 1

    
    def iscomplete(self):
        if '_' not in self.wordscreen or self.stages == 6: return True
        else: return False
