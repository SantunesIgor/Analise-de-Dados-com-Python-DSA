mylista = [[1,2,3], [4,5,6], [7,8,9]]
mylistb = [[9,8,7], [6,5,4], [3,2,1]]
mylistc = mylista + mylistb
mylistd = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myliste = []

print('---------------')
print(mylista[0][0])
print(mylistc)
print(10 in mylista)
print(9 in mylista[2])
print(len(mylista))
print(len(mylistd))
print(max(mylistd))
print(min(mylistd))
print(mylistd.index(5))

myliste.append(1)
myliste.append(1)
print(myliste)
print(myliste.count(1))
myliste.remove(1)
print(myliste)

for i in mylistd:
    myliste.append(i)
print(myliste)

mylistd.insert(2, 10)
print(mylistd)

mylistd.reverse()
print(mylistd)

mylistd.sort()
print(mylistd)

print(min(mylistd))
print(max(mylistd))
print(sum(mylistd))

print('---------------')