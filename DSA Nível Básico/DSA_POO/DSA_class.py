class Livro():
    def __init__(self):
        self.titulo = 'O Timbre'
        self.code = 1231241
        print('Builder')

livro = Livro()
print(type(livro))
print(livro.titulo)
print(livro.code)

print("----------------------")
class Livro_():
    def __init__(self, title, code):
        self.title = title
        self.code = code
        print('builder has been run')

livro = Livro_('O Timbre', '1231241')
print(livro)
print(livro.title)
print(livro.code)

print("----------------------")
class Class():
    def __init__(self, z):
        self.z = z
        print('builder has been run')
    
x = Class('y')
y = Class(z = 'x')

print(x.z)
print(y.z)

print("----------------------")