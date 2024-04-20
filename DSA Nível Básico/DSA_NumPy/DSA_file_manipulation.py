import os, numpy as np

dataset = os.path.join('Archives/dataset.csv') # abre o arquivo
array = np.loadtxt(dataset, delimiter = ',', usecols = (0, 1, 2, 3), skiprows = 1) #dataset = define o arquivo, delimiter define oque separa as colunas, usecols = quais colunas serão usadas e skiprows = quais linhas serão puladas, geralmente usado para pular a linha de título
print(array)

array_1, array_2 = np.loadtxt(dataset, delimiter=',', usecols=(0, 1), skiprows=1, unpack=True) # a unpack true separa as 2 colunas em 2 arrays diferentes
print(array_1)
print(array_2)

