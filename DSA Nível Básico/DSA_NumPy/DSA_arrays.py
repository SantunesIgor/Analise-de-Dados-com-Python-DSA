import numpy

print('----------------------')

array = numpy.array([10, 21, 32, 43, 54, 65, 76, 87, 98])
list = [10, 21, 32, 43, 54, 65, 76, 87, 98]

print(array)
print(type(array))
print(array.shape)
print(array[4])
print(array[1:4])
print(array[1:4+1])

array2 = numpy.array([10, 21, 32, 43, 54, 65, 76, 87, 98])
print(array + array2)
list2 = [10, 21, 32, 43, 54, 65, 76, 87, 98]
print(list + list2)

index = [1, 2, 3, 4]
print(array[index])

mask = (array % 2 == 0)
print(mask)
print(array[mask])

array[0] = 100
print(array)

# apenas do tipo criado originalmente
try: array[0] = 'New Element'
except: print('Operantion not allowed')

array = numpy.array(['a', 'b', 'c', 'd', 'e'])
print(array)
array[0] = 'New Element'
print(array) # retorna apenas o n porque como a string 'a' tem só uma letra, ele vai adicionar apenas uma letra também