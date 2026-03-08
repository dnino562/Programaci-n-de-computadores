def mayor_de_tres_numeros(numero1, numero2, numero3):
    return max(numero1, numero2, numero3)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print("El número mayor es:", mayor_de_tres_numeros(num1, num2, num3))