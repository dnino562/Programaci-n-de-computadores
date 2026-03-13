from empleado import Empleado

class EmpleadoFijo(Empleado):

    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual