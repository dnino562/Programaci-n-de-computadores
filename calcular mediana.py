#Crea una función llamada "calcular_mediana" que toma un número variable de parámetros y devuelve la mediana de los números. La mediana es el número que se encuentra en el medio de la lista ordenada. Si la lista tiene un número par de elementos, la mediana es el promedio de los dos números del medio.
def calcular_mediana(*numeros):
    lista = list(numeros)
    lista.sort()
    n = len(lista)

    if n % 2 == 1:
        mediana = lista[n // 2]
    else:
        mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2

    return mediana


print(calcular_mediana(3, 1, 4, 2))
print(calcular_mediana(3, 1, 4, 2, 6))