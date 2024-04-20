class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self): # reescrita da classe para mudar oque ela retorna
        return "Au Au!"

cachorro = Cachorro("Buddy")
print(cachorro.nome) # usamos a var nome mesmo sem que ele esteja na classe Cachorro, já que ele 'herda' da classe animal
print(cachorro.fazer_som())
