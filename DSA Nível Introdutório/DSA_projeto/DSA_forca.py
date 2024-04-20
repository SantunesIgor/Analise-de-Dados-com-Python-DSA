import random
from os import system, name
import re

stages = [
    '--------------\n|           |\n|           \n|           \n|           \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|           \n|           \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|           |\n|            \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|          /|\n|            \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|          /|\\\n|            \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|          /|\\\n|          / \n|\n|\n--------------',
    '--------------\n|           |\n|           O\n|          /|\\\n|          / \\\n|\n|\n--------------'
]

def forca(x):
    print('Letras erradas:', ' '.join(letterlist))
    print(stages[x])
    if x == 6: print('Você perdeu! A palavra era:', key)
    else: print('Palavra:', ' '.join(keyeye))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def chose_word():
    words = ['banana', 'uva', 'abacaxi', 'laranja', 'manga', 'tomate', 'morango']
    return random.choice(words)

def exeption(x):
    clear()
    print(x)

key = chose_word()
keyeye = ['_' for _ in key]
letterlist = []
count = 0

while count != 6:
    forca(count)

    if '_' not in keyeye: 
        print('\nParabéns, a palavra era:', key)
        break

    letter = input('Digite uma letra: ')

    if letter not in re.findall(r'[a-z]', letter):
        exeption('Resposta não permitida')
        continue

    if letter not in letterlist: letterlist.append(letter)
    else: 
        exeption('Essa letra já foi!')
        continue

    keyeye = [k if k == letter else e for k, e in zip(list(key), keyeye)]

    if letter not in list(key):
        count += 1

    clear()

forca(count)