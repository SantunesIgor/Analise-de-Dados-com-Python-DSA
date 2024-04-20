import numpy

arr = numpy.arange(1, 10) # função range com array
print(arr)
print(numpy.sum(arr)) # soma de todos os elementos
print(numpy.prod(arr)) # produto de todos os elementos
print(numpy.cumsum(arr)) # soma gradual de todos os elementos
print(numpy.cumprod(arr)) # produto gradual de todos os elementos

print("----------------------")

arr = numpy.array([1, 2, 3])
arr2 = numpy.array([3, 2, 1])
print(numpy.add(arr, arr2)) # adiciona os elementos com o mesmo índice

print("----------------------")

arr = numpy.array([[1, 2], [3, 4]])
arr2 = numpy.array([[5, 6], [7, 8]])
print(arr.shape)
print(arr2.shape)
print(arr)
print(arr2)
print(numpy.dot(arr, arr2)) # multiplica as matrizes
print(arr @ arr2) # mesma coisa

print("----------------------")

arr = numpy.array([1, 2])
arr2 = numpy.array([5, 7])
print(numpy.dot(arr, arr2)) # multiplica as matrizes

