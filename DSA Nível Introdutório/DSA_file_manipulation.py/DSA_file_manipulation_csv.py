# print('---CSVFILE--CSVFILE---CSVFILE---')

# print('linha-unica--------')
# f = open("salarios.csv", 'r')
# data = f.read()
# rows = data.split('\n')
# print(rows)

# print('colunas--------')
# f = open("salarios.csv", 'r')

# data = f.read()
# rows = data.split('\n')
# full_data = []

# for rows in rows:
#     split_rows = rows.split(',')
#     full_data.append(split_rows)
#     first_row = full_data[0]
# print(full_data)
# count = 0

# for row in full_data:
#     count += 1

# count = 0

# for column in first_row:
#     count += 1

# print(count)

# f.seek(0,0)
# print(f.readlines())

print('---CSVFILE--csv---')
import csv

with open('numeros.csv', 'w') as arq:
    writer = csv.writer(arq)
    writer.writerow(('Nota 1', 'Nota 2', 'Nota 3'))
    writer.writerow((6, 8, 5))
    writer.writerow((8, 10, 4))

with open('numeros.csv', 'r', encoding='utf8', newline='\r\n') as arq:
    leitor = csv.reader(arq)
    dados = []
    for i in leitor:
        dados.append(i)
        print(i)

print(dados)

for i in dados[1:]:
    print(i)
    