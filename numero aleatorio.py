import random

def num_aleatorio():
    numero = random.randint(1,100)
    intento = int(input("Adivina el número entre 1 y 100: "))
    
    if intento == numero:
        print("¡Felicitaciones, adivinaste el número!")
    elif intento > numero:
        print("El número que ingresaste es mayor que el número secreto")
    else:
        print("El número que ingresaste es menor que el número secreto")

num_aleatorio()