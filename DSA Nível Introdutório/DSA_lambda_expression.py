def pot0(x):
    a = x ** 2
    return a

def pot1(x):
    return x ** 2

def pot2(x): return x ** 2

print(pot0(5))
print(pot1(5))
print(pot2(5))

pot3 = lambda x: x ** 2
print(pot3(5))

par = lambda x: x % 2 == 0
print(par(2))

fst = lambda x: x[0]
print(fst('Deus'))

som = lambda x, y: x + y
print(som(2, 2))
