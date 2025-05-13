class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self, largura, altura):
         super().__init__()
         self.largura = largura
         self.altura = altura

    def CalcularArea(self):
         self.area = self.largura * self.altura
         print(f"Área do Retângulo: {self.area}")

    def CalcularPerimetro(self):
        self.perimetro = 2 * (self.largura + self.altura)
        print(f"Perímetro do Retângulo: {self.perimetro}")

class Triangulo(Forma):
    def __init__(self, base, altura):
      super().__init__()
      self.base = base
      self.altura = altura

    def calcularArea(self):
       self.area = (self.base * self.altura) / 2
       print(f"Área do Triângulo: {self.area}")

    def calcularPerimetro(self, lado1, lado2):
        self.perimetro = self.base + lado1 + lado2
        print(f"Perímetro do Triângulo: {self.perimetro}")