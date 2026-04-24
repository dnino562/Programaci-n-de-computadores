def menu():
    opcion = -1
    while opcion < 1 or opcion > 4:
        print("-- MENU DE FIGURAS --")
        print("1. Triangulo centrado")
        print("2. Triangulo invertido centrado")
        print("3. Triangulo alineado a la derecha")
        print("4. Triangulo alineado a la izquierda")
        opcion = int(input("Seleccione una opcion: "))
    return opcion

def figura1(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def figura2(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def figura3(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("  ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def figura4(n):
    for i in range(n, 0, -1):
        for k in range(i):
            print("* ", end="")
        print()

opcion = -1
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        print("\nFigura 1:")
        figura1(5)
        
    elif opcion == 2:
        print("\nFigura 2:")
        figura2(5)
        
    elif opcion == 3:
        print("\nFigura 3:")
        figura3(5)
        
    elif opcion == 4:
        print("\nFigura 4:")
        figura4(5)
        
print("\nHasta luego!")