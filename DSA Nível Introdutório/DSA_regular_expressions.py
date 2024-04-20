import re

texto = 'deus e bom e o diabo nao presta'
print(re.findall(r'diabo (\w+) (\w+)', texto))

email = 'igorsantunes@outlook.com, santunesigor@gmail.com, palavra'
print(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))

anosluz = '''
Estamos anos luz daquele lugar
Nem sei como eu vim parar aqui
Tua língua eu não entendo
Eu só sei que tu é chata e muito gata pra mim
Eu vim de lá, eu vim de longe, de longe de cá
Eu vim pra te ensinar que quando o beat dropa a gente nunca mais pode parar (tsey)

E quando a gente cai na cama
O bagulho esquenta quente na frigideira (quente na frigideira)
Quando eu bato o olho nela não paro de imaginar besteira (eu só penso besteira)
Sinceramente, o problema é ela porque essa bunda é brincadeira (essa bunda é brincadeira)
Quem ela pensa que é esfregando essa porra em mim a noite inteira

Dropando o doce em mim a noite inteira
Fumando um beckzinho a noite inteira
Tô com ela em um foguete de bobeira
Ta me enlouquecendo mesmo que eu não queira (mesmo que eu não queira)

A 30 contra tudo
A 30 contra o mundo

E o que que eles vão falar? (fala pra mim)
Se agora a gente tá de alta
Vagabundo se exalta (de alta)
Daqui uns anos eu sei quem que vai sobrar (quem?)
Dinheiro pra gente vai sobrar
Lama no copo pra gente vai sobrar (quem?)
Quem não tava com a gente vai sobrar
E muito bagulho pra gente assoprar
Tive um déjà vu que nós entrava numa grife e assaltava tudo
Eu nunca deixo ela no tédio, alugo um privado e vamos para Búzios
Tem spa e um estúdio, vamo dominar o mundo
Avançamos anos luz e a 30 comandando tudo no futuro

Estamos anos luz daquele lugar
Nem sei como vim parar aqui
Tua língua eu não entendo
Eu só sei que tu é chata e muito gata pra mim
Eu vim de lá, eu vim de longe, de longe de cá
Eu vim pra te ensinar que quando o beat dropa a gente nunca mais pode parar (tsey)

E quando a gente cai na cama o bagulho esquenta quente na frigideira
(Quente na frigideira)
Quando eu bato o olho nela não paro de imaginar besteira (eu só penso besteira)
Sinceramente o problema é ela porque essa bunda é brincadeira (essa bunda é brincadeira)
Quem ela pensa que é esfregando essa porra em mim a noite inteira

Dropando o doce e minha a noite inteira
Fumando um beckzinho a noite inteira
Tô com ela em um foguete de bobeira
Ta me enlouquecendo mesmo que eu não queira (mesmo que eu não queira)

E o que que eles vão falar?
Daqui uns anos eu sei quem que vai sobrar
Avançamos anos luz e a 30 comandando tudo no futuro

Dropando um doce em mim a noite inteira
Fumando um beckzinho a noite inteira
Tô com ela em um foguete de bobeira
Ta me enlouquecendo mesmo que eu não queira (mesmo que eu não queira)
'''

print(anosluz.count('a'))
print(anosluz.count('anos'))
print(re.findall(r'\((.*)\)', anosluz))
print(re.findall(r'(?:anos\s+)(\w+)', anosluz))
print(re.findall(r'[\w+]+[áéíóúãõâêîôûàèìòùäëïöüç]', anosluz))
