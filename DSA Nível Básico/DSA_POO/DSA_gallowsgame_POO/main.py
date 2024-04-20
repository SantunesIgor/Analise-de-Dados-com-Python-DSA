from word import Word
from screen import Screen

key = Word(['banana', 'apple', 'orange', 'watermelon', 'strawberry', 'grape', 'mango', 'pineapple', 'lemon', 'avocado', 'raspberry', 'cherry'])

while Word.iscomplete(key) == False:
    Screen.clear()
    Screen(key.stages, key.wordscreen, key.letterlist, key.code)
    Word.letter(key, letter=input('Try a letter: '))

Screen.final(key, key.word, key.stages)