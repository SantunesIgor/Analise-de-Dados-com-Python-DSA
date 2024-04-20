def som(x, y):
    print('%f + %f = %f' %(x, y, x + y))

def sub(x, y):
    print('%f - %f = %f' %(x, y, x - y))

def mul(x, y):
    print('%f * %f = %f' %(x, y, x * y))

def div(x, y):
    print('%f / %f = %f' %(x, y, x / y)) 

print('---CALCULADORA--------------------')

while True:
    try:
        x = float(input('Digite o primeiro número: '))
        opr = input('Digite a operação (+, -, *, /): ')
        y = float(input('Digite o segundo número: '))
    except:
        print('Input inválido')
        continue

    if opr == '+': som(x, y)
    elif opr == '-': sub(x, y)
    elif opr == '*': mul(x, y)
    elif opr == '/': div(x, y)
    else: print('Operação inválida')