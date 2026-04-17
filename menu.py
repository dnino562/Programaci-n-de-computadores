nombre = ""
edad   = 0

def mostrarMenu():
    print("\n===== MENÚ =====")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

while True:
    opcion = mostrarMenu()

    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        edad   = int(input("Ingrese su edad: "))
        print("Datos guardados correctamente.")
    elif opcion == 2:
        print(f"Nombre: {nombre}")
        print(f"Edad  : {edad}")
    elif opcion == 3:
        print("Hasta luego.")