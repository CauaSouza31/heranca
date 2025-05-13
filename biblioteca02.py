class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    def ImprimeValor(self):
        print(f"Valor do ingresso: R$ {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor*=1.5

    def ValorVip(self):
        print(f"Valor do ingresso VIP: R$ {self.valor}")
