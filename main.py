from empleado_fijo import EmpleadoFijo
from empleado_horas import EmpleadoPorHoras
from empresa import Empresa


empresa = Empresa()

e1 = EmpleadoFijo("Ana",3000)
e2 = EmpleadoPorHoras("Luis",80,20)

empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)

print("Nomina:",empresa.calcular_nomina())
print("Salario e1:", e1.calcular_salario())
print("Salario e2:", e2.calcular_salario())