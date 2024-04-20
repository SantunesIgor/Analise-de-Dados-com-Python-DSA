import math

def prime(x, y):
    prime = []
    for i in list(range(x, y)):
        divisor = []
        a = 1
        while a != i:
            if i % a == 0:
                divisor.append(a)
            a += 1
        if len(divisor) < 2:
            prime.append(i)
    return prime

def primes_for(x, y):
    primelist = []
    for i in list(range(x, y)):
        divisorslist = []
        for j in list(range(1, i)):
            if i % j == 0:
                divisorslist.append(j)
        if len(divisorslist) < 2:
            primelist.append(i)
    return primelist

def mathprime(x):
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

x = primes_for(1, 100)
print('Primes For: ', x)


x = prime(1, 100)
print('Primes: ', x)

print(mathprime(int(input('Digite o número que deseja saber se é primo: '))))

