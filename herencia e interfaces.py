from abc import ABC, abstractmethod
class Figura (ABC):
    @abstractmethod
    def area (self):
        pass
    
class Cuadrado(Figura):
    
    def __init__(self, lado):
        self.lado=lado
        
    def area(self):
        return self.lado * self.lado

class Circulo (Figura):
    
    def __init__(self, radio):
        self.radio=radio
        
    def area(self):
        return self.radio * self.radio * 3.1416

figuras=[Cuadrado(4), Circulo(3)]

for f in figuras:
    print(f"Área:{f.area()}")