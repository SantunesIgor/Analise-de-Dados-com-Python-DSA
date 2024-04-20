print('---TEXTFILE--TEXTFILE---TEXTFILE---')

print("READ-'r'------------")
arq = open("DSA_arquivo_1.txt", 'r')

print(type(arq))
print(arq.read())
print(arq.tell())
print(arq.read())

arq.seek(0,0)
print(arq.read())

arq.seek(0,0)
print(arq.read(10))

arq.close

print("WRITE-'r'-----------")
arq = open("DSA_arquivo_2.txt", 'w')
arq.write("Deus e bom")

arq.close
arq = open("DSA_arquivo_2.txt", 'r')
print(arq.read())

print("APPEND-'a'-----------")
arq = open("DSA_arquivo_2.txt", 'a')
arq.write(' e o diabo nao presta')

arq.close
arq = open("DSA_arquivo_2.txt", 'r')
print(arq.read())

print('---TEXTFILE--PACKOS------')

txt = 'Deus e bom '
txt += 'e o diabo nao presta '

import os

arq = open(os.path.join('DSA_arquivo_3.txt'), 'w')
arq.write(txt)

print('---TEXTFILE--with------')
with open('DSA_arquivo_3.txt', 'r') as arq:
    read = arq.read()
print(read)

with open('DSA_arquivo_4.txt', 'w') as arq:
    arq.write('Deus e bom e o diabo nao presta')

arq = open('DSA_arquivo_4.txt', 'r')
print(arq.read())
