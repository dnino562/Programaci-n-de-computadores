from empleado import Empleado

class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, horas, valor):
        super().__init__(nombre)
        self.horas = horas
        self.valor = valor

    def calcular_salario(self):
        return self.horas * self.valor