class Employee():
    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage

mr_charles = Employee('charles', 27, 2574)

#hasattr(var, attr) - Verifica se há o atributo
print(hasattr(mr_charles, 'name'))

#setattr(var, attr, newvalue) - Muda o valor do atributo
setattr(mr_charles, 'wage', 4500)
print(mr_charles.wage)

#delatrr(var, attr) - Deleta o atributo
delattr(mr_charles, 'wage')
print(hasattr(mr_charles, 'wage'))