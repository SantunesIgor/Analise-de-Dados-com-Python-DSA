print("MAP")

def pot(x): return x ** 2
print(list(map(pot, range(101))))

Celsius = range(101)
print(list(map(lambda x: (x * 9/5) + 32, Celsius)))

a = range(1, 5)
b = range(5, 9)

print(list(map(lambda x,y: x + y, a, b)))

print("REDUCE")

from functools import reduce

exlist = range(1, 11)

def soma(a, b): return a + b

print(reduce(soma, exlist))

print(reduce(lambda x, y: x + y, exlist))

maxfind = lambda a, b: a if (a > b) else b

print(reduce(maxfind, exlist))

print("FILTER")

def verpar(x):
    if x % 2 == 0: return True
    else: return False

print(verpar(26))

exlist = range(1, 19)

print(list(filter(verpar, exlist)))
print(list(filter(lambda x: x % 2 == 0, exlist)))

print("ZIP")

a = ['1', '2', '3']
b = ['4', '5', '6']

print(list(zip(a, b)))
print(list(zip('ABCD', 'EF')))

a = {'a': 'A', 'b': 'B'}
b = {'c': 'C', 'd': 'D'}

print(list(zip(a, b)))
print(list(zip(a, b.values())))

print("ENUMERATE")

a = ['a', 'b', 'c']
print(list(enumerate(a)))

for i, v in enumerate(a):
    print(i, v)

