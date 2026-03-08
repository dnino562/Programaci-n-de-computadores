def calcular_area(radio, altura):
    area = 2 * 3.14 * radio * altura + 2 * 3.14 * radio ** 2
    return area

radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

print("El área del cilindro es:", calcular_area(radio, altura))