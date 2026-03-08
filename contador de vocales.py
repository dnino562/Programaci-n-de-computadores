def contador_vocales():
    texto = input("Ingrese una cadena: ")
    contador = 0
    
    for letra in texto:
        if letra in "aeiouAEIOU":
            contador += 1
    
    return contador

print("Número de vocales:", contador_vocales())