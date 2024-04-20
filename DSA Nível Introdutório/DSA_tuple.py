tuple1 = ('Geografia', 'Elefante', 'Python')

print('---------------')
print(tuple1)

# tuple.append('Chocolate') - Não é possível alterar coisas nas tuplas

print(tuple1[0])
print(len(tuple1))
print(tuple1[1:])

list = list(tuple1)
print(list)
tuple1 = tuple(list)
print(tuple1)
print('---------------')