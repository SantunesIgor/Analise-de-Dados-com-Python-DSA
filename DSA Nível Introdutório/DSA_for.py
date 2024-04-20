numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numb2 = [2, 4, 6, 8, 10]

print('---------------')
for i in numb:
    print(i)

print('---------------')
for i in range(1, 11):
    print(i)

print('---------------')
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print('---------------')
for i in range(0, 101, 2):
    print(i)

print('---------------')
for i in numb and numb2:
    print(i)

print('---------------')
for i in numb:
    for j in numb2:
        print(i * j)
    
print('---------------')
# loop through lists to find the higher number
m = [[-12, -23, -34], [-45, -56, -67], [-78, -89, -90]]
hn = m[0][0]

for i in m:
    for j in i:
        if j > hn:
            hn = j
print(hn)

print('---------------')
dict = {'Camila': 19, 'Hugo': 32, 'Flávio': 21}
for a, b in dict.items():
    print(a, b)

print('---------------')
a = 'Deus é bom e o diazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzbo não presta'
for i in a:
    if i == 'z':
        continue
    print(i)

print('---------------')