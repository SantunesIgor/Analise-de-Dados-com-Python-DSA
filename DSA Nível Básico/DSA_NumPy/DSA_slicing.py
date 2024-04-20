import numpy as np

arr = np.diag(np.arange(3)) # cria uma matrix de zeros com os numeros de 0 a 2 nas diagonal principal
print(arr)
print(arr[1, 1]) # linha de index 1 e coluna de indez 1
print(arr[1]) # toda a linha de index 1
print(arr[:,2]) # toda a coluna de index 2

print("----------------------")

arr = np.arange(10) # create a array with numbers from 0 to 9
print(arr)
print(arr[2:9:3]) # get numbers 2 to 9 skipping 3 numbers

print("----------------------")

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(a == b) # checks if each index of a array is equal to index from another array
print(np.equal(a, b)) # does the same thing
print(a.max()) # get the largest number in the array
print(a.min()) # get the smallest number in the array

print("----------------------")

arr = np.array([1, 2, 3]) + 1.5 # add 1.5 to each element in the array
print(arr)

print("----------------------")

arr = np.array([1.2, 1.5, 2.3, 4.5, 5.4, 5.6, 8.6])
print(arr)
print(np.around(arr)) # rounds each element of the array

print("----------------------")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print(arr.flatten()) # joins the collunms of the array

print("----------------------")

arr = np.array([1, 2, 3])
print(arr)
print(np.repeat(arr, 3)) # repeats each element of the array as many times as desired, in this case, 3
print(np.tile(arr, 3)) # repeats the array 3 times

print("----------------------")

arr = np.array([5, 6])
print(arr)
arr2 = np.copy(arr) # copies the array
print(arr2)

print("----------------------")