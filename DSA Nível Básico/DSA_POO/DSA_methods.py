import math

# método é mesma coisa que função, porem a função é feita independente, o método depende da classe

class Circle():
    def __init__(self, radius = 5):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi
    
    def circ(self):
        return 2 * math.pi * self.radius
    
circle = Circle() # define 'circle' como objeto da classe Circle
print(circle.radius) # define o radius igual a 5, já que não foi passado nenhum valor
print(circle.area()) # vai para o método 'area' e retorna oque nela contém
print(circle.circ())

print('---------------')

circle = Circle(7) # agora o raio é 7, e não 5, já que agora foi definido um valor
print(circle.radius)
print(circle.area())
print(circle.circ())