import numpy

array = numpy.array([[1,2,3], [4,5,6]]) # cria uma array, nesse caso, de 2 linhas e 3 colunas
print(array)
print(array.shape)
print(type(array))

ones = numpy.ones((2,3)) # cria uma matriz de 'uns' com linhas colunas que desejar
print(ones)

matrix = numpy.matrix([[1,2,3], [4,5,6], [7,8,9]]) # cria uma matriz 3x3
print(matrix)
print(type(matrix))
print(matrix.shape)
print(matrix.size)
print(array.dtype)

print(matrix[2, 1])
print(matrix[0:2, 2])
print(matrix[1,])

matrix[1, 0] = 100
print(matrix)

array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype = numpy.float64) # forçando o datatype da array
print(array)
print(array.dtype)

print(array.itemsize) # bytes que cada elemento ocupa no disco
print(array.nbytes) # bytes que a array ocupa no disco
print(array.ndim) # numero de dimenções, nesse caso, como é uma linha, apenas uma