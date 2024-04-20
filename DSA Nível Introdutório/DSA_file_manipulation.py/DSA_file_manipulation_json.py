import json

dicty = {'nome': 'Igor', 'linguagem': 'python', 'idade': 17, 'escola:': 'DSA'}

with open('DSA_arquivo_5.json', 'w') as arq:
    arq.write(json.dumps(dicty))

with open('DSA_arquivo_5.json', 'r') as arq:
    print(json.loads(arq.read()))

print(dicty['nome'])