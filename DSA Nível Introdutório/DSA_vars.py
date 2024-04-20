a = 0 # var goblal

def printn(x, y):
    a = x * y
    print(a) # var local

def printm(x, y):
    b = x * y
    print(b)

printn(5, 5) # var local
print(a) # var goblal
printm(5, 6)
#print(b) Variável não reconhecida