from abc import ABC, abstractmethod
class Empleado(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    @abstractmethod
    def calcular_salario(self):
        pass