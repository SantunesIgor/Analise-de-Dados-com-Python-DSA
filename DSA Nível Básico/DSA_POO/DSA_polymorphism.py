class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print('o carro está acelerando')

    def frear(self):
        print('o carro está freando')

class Aviao(Veiculo):
    def acelerar(self):
        print('o aviao está acelerando')

    def frear(self):
        print('o aviao está freando')

    def decolar(self):
        print('o aviao esta decolando')

lista_veiculos = [Carro('Dodge', 'Challenger'), Aviao('Boeing', '757')]

for i in lista_veiculos:
    i.acelerar()
    i.frear()

    if isinstance(i, Aviao):
        i.decolar()
    
    print('---------------')