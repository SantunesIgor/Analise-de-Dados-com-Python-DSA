import numpy

array = numpy.array([1, 2, 3, 4])

print(array.cumsum()) # soma acumulada
print(array.cumprod()) # multiplicação acumulada

array = numpy.arange(0, 50, 5) # mesma idéia da função 'range', mas cria uma array em cima
print(array)
print(array.shape) # retorna as dimenções da array (linhas, colunas, ...)
print(array.dtype) # tipo de dado da array

array = numpy.zeros(10) # retorna 10 zeros em forma de array
print(array)

array = numpy.eye(3) # retorna uma matriz de 0, com a diagonal principal sendo de 1 
print(array)

array = numpy.diag(numpy.array([1, 2, 3, 4])) # retorna uma matriz de 0, com a diagonal principal sendo dos valores das matrizes
print(array) 

print(numpy.linspace(1, 10)) # retorna uma array de 50 numeros situados na mesma distancia entre si entre os numeros 1 e 10
print(len(numpy.linspace(1, 10)))
print(numpy.linspace(1, 10, 10)) # mesmo esquema, só que agora apenas 10 numeros, já que foi definido assim

print(numpy.logspace(0, 5, 10)) # mesmo esquema, só que em logaritimo