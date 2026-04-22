def mostrar_menu() -> int:
    print("===== MENÚ PRINCIPAL =====")
    print("1. Mostrar números (for)")
    print("2. Sumar números (while)")
    print("3. Validar contraseña (do-while)")
    print("4. Salir")
    return int(input("Elige una opción: "))

#  Opción 1 – Mostrar números con FOR

def mostrar_numeros(n):
    print(f"Números del 1 al {n}:")
    for i in range(1, n + 1):
        print(i)


#  Opción 2 – Sumar números con WHILE

def sumar_numeros():
    suma = 0
    print("Ingrese números para sumar (0 para terminar):")
    while True:
        numero = int(input())
        if numero == 0:
            break
        suma += numero
    return suma



#  Opción 3 – Validar contraseña con DO-WHILE

def validar_password():
    PASSWORD_CORRECTA = "123"
    print(" Acceso restringido")
    
    while True:                              
        intento = input("Ingresa la contraseña: ")
        if intento == PASSWORD_CORRECTA:
            break                            
        print("Contraseña incorrecta. Intenta de nuevo.")
    print("¡Acceso concedido! Bienvenido.")

opcion = 0
while opcion != 4:
    opcion = mostrar_menu()
    
    if opcion == 1:
        n = int(input("¿Hasta qué número quieres mostrar? "))
        mostrar_numeros(n)

    elif opcion == 2:
        total = sumar_numeros()
        print(f"La suma total es:", total)

    elif opcion == 3:
        validar_password()

    elif opcion == 4:
        print("¡Hasta luego! Programa finalizado.")

    else:
        print("Opción no válida. Intenta de nuevo.")
 