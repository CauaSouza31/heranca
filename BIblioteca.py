class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def Comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Miar(self):
        print(f"O {self.nome} foi miar")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def ComerCapim(self):
        print(f"O {self.nome} foi comer urtiga")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Latir(self):
        print(f"O {self.nome} foi latir")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Pular(self):
        print(f"O {self.nome} foi pular")

class Galinha(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Voar(self):
        print(f"a {self.nome} foi voar")





