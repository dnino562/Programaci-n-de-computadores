def contar_ocurrencias(cadena, palabra):
    return cadena.count(palabra)

cadena = "hola,hola,hola"
palabra = "hola"

print("Número de veces que aparece:", contar_ocurrencias(cadena, palabra))