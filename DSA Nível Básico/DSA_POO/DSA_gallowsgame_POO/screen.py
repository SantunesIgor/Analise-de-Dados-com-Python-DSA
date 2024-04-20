from os import system, name

class Screen():
    global gallows
    gallows = [
        '--------------\n|           |\n|           \n|           \n|           \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|           \n|           \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|           |\n|            \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|          /|\n|            \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|          /|\\\n|            \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|          /|\\\n|          / \n|\n|\n--------------',
        '--------------\n|           |\n|           O\n|          /|\\\n|          / \\\n|\n|\n--------------'
    ]

    def __init__(self, stages, wordscreen, letterlist, especialcode):
        self.wordscreen = wordscreen
        self.letterlist = letterlist
        self.stages = stages

        if especialcode == 1: print("This letter isn't allowed")
        elif especialcode == 2: print("You tried this letters already")

        print('Letters tried:', ' '.join(self.letterlist))
        print(gallows[stages])
        print('Word:', ' '.join(self.wordscreen))

    def final(self, word, stages):
        self.word = word
        if stages != 6: 
            Screen.clear()
            print(gallows[stages])
            print('Congratulations! The word was:', self.word)
        else: 
            Screen.clear()
            print(gallows[stages])
            print('You lost! The word was:', self.word)

    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')