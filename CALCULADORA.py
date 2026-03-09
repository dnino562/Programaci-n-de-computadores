import math

class Calculadora:

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def division_entera(self, num1, num2):
        return num1 // num2

    def modulo(self, num1, num2):
        return num1 % num2

    def potencia(self, num1, num2):
        return num1 ** num2

    def raiz_cuadrada(self, num):
        return math.sqrt(num)


calculadora = Calculadora()

print("Suma:", calculadora.sumar(4, 3))
print("Resta:", calculadora.restar(5, 7))
print("Multiplicación:", calculadora.multiplicar(4, 6))
print("División entera:", calculadora.division_entera(10, 4))
print("Módulo:", calculadora.modulo(25, 2))
print("Potencia:", calculadora.potencia(3, 4))
print("Raíz cuadrada:", calculadora.raiz_cuadrada(49))