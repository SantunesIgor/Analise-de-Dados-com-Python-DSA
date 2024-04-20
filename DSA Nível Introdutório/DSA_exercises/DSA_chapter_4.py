print('---------------')
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
a = list(range(1, 11))
print('exercise 1: ', a)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
b = ['A', 'B', 'C', 'D', 'E']
print('exercise 2: ', b)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
a = 'Deus é bom e o '
b = 'diabo não presta'
c = a + b
print('exercise 3: ', c)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do objeto tupla para verificar 
# quantas vezes o número 4 aparece na tupla
d = (1, 2, 2, 3, 4, 4, 4, 5)
print('exercise 4: ', d.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
e = {}
print('exercise 5: ', e)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
f = {'Camila': 19, 'Hugo': 32, 'Flávio': 21}
print('exercise 6: ', f)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
f['Julia'] = 43
print('exercise 7: ', f)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. Imprima o dicionário na tela.
g = {'Números': [1, 2], 'Glock': 'Bandido', 'Rock': 'Música'}
print('exercise 8: ', g)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float. Imprima a lista.
h = ['Água', (1, 2), {'A': 'a', 'B': 'b'}, 4.1239]
print('exercise 9: ', h)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
i = 'Deus é bom e o diabo não presta'
print('exercise 10: ', i[1:19])
print('---------------')