def helloword():
    print('hello word')

def printname(name):
    print('Your name is', name)

def printnumbers(x, y):
    for i in list(range(x, y)):
        print(i)

def multiargs(*vartuple):
    print(vartuple)

helloword()
printname('Igor')
printnumbers(1, 6)
multiargs('Son', 'of', 'God')
multiargs('Jesus', 'Christ')