def buscar_palabra(cadena, palabra):
    return palabra in cadena

cadena = input("Ingrese una frase: ")
palabra = input("Ingrese la palabra a buscar: ")

print(buscar_palabra(cadena, palabra))