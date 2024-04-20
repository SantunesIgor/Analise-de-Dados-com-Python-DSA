age_dict = {'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Julia': 25}
age_dict_2 = {'Camila': 19, 'Hugo': 32, 'Flávio': 21}
lists_dict = {'Comidas': ['Arroz', 'Carne'], 'Bebidas': ['Suco', 'Refrigerante'], 'Números': [1, 2, 3]}
dict = {}

print('---------------')
print(age_dict)
print(age_dict['Ana'])

age_dict['Marcelo'] = 23
print(age_dict['Marcelo'])

print(len(age_dict))
print(age_dict.keys())
print(age_dict.values())
print(age_dict.items())

age_dict.update(age_dict_2)
print(age_dict)

a = age_dict['Ana']
b = age_dict['Marcelo']
c = age_dict['Ronaldo']
print(a, b, c)

age_dict.clear()
print(age_dict)

print(lists_dict['Bebidas'])
print(lists_dict['Bebidas'][0])
print(lists_dict['Bebidas'][0].upper())

a = lists_dict['Números'][0] - 1
print(a)

# dict['age_dict'] = age_dict
# dict['age_dict_2'] = age_dict_2
# dict['lists_dict'] = lists_dict
dict = {'age_dict': age_dict, 'age_dict_2': age_dict_2, 'lists_dict': lists_dict}
print(dict)
print('---------------')