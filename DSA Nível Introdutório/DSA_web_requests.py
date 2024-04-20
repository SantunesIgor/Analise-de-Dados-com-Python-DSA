from urllib.request import urlopen
import json

response = urlopen('http://www.omdbapi.com/?apikey=2dd4326c&t=Titanic&type=movie').read().decode('utf8')
data = json.loads(response)
print(data)

print('Título: ', data['Title'])
print('Ano: ', data['Year'])
print('Gênero: ', data['Genre'])

with open('DSA_arquivo_json.json', 'w') as arq: arq.write(str(response))

with open('DSA_arquivo_json.json', 'r') as jsonarq:
    jsoncont = json.loads(jsonarq.read())
    with open('DSA_arquivo_6.text', 'w') as textarq:
        for k, v in jsoncont.items():
            textarq.write('%s: %s;\n' %(k, v))

open('DSA_arquivo_7.text', 'w').write(open('DSA_arquivo_json.json', 'r').read())

with open('DSA_arquivo_7.text', 'r') as arq:
    jsontext = arq.read()
    dicty = json.loads(jsontext)
    print(dicty)