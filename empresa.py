class Empresa:

    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, empleado):
        self.empleados[empleado.nombre] = empleado

    def calcular_nomina(self):
        total = 0
        for emp in self.empleados.values():
            total += emp.calcular_salario()
        return total