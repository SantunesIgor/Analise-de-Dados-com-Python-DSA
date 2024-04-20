# É um loop dentro de um lista, a criação de uma com a função for

lista = [x for x in range(10)]
print(lista)

listb = [x for x in range(10) if x % 2 == 0]
print(listb)

stra = 'Deus é bom e o diabo não presta'
listc = [x for x in stra if 'a' in x]
print(listc)

listd = [x for x in range(1, 101) if x % 4 == 0]
print(listd)

dictex = {'Jorge': 10, 'Isabela': 7, 'Matheus': 5, 'Douglas': 8, 'Raissa': 9}
dicta = {k:v for (k, v) in dictex.items() if v >= 7}
print(dicta)

dictb = {k: 'Aprovado' if v >= 7 else 'Reprovado' for (k, v) in dictex.items()}
print(dictb)