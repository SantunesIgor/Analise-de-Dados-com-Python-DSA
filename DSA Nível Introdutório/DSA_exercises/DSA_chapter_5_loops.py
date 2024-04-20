# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
print('Exercício 1 -----')
a = input('Qual o dia da semana? ')
print(a)
if a == 'domingo' or a == 'sábado':
    print('dia de descanço')
else:
    print('dia de trabalhar')

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
print('Exercício 2 -----')
a = ['morango', 'maçã', 'pera', 'banana', 'uva']
for i in a:
    if i == 'morango':
        print('tem morango na lista')
        break
    print('não tem morango na lista')
    
print('Exercício 3 -----')
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
a = (1, 2, 3, 4)
b = []
for i in a:
    b.append(i * 2)
print(b)

print('Exercício 4 -----')
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151, 2):
    print(i)

print('Exercício 5 -----')
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temp = 40
# while temp > 35:
#     print(temp) vai ficar pra sempre isso aqui

print('Exercício 6 -----')
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
cont = 0
while cont < 100:
    print(cont)
    if cont == 23:
        break
    cont += 1

print('Exercício 7 -----')
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
a = []
b = 4
while b <= 20:
    if b % 2 == 0:
        a.append(b)
    b += 1
print(a)

print('Exercício 8 -----')
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = [i for i in range(5, 45, 2)]
print(nums)

print('Exercício 9 -----')
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print('Exercício 10 -----')
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
print("A letra 'r' aparece %i vezes" %(frase.count('r')))