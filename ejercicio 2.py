carnes = {"lomo": 25000, "costilla": 28000, "solomo": 20000, "punta": 30000, "paleta": 27000}

tipo = input("Ingrese el tipo de carne: ")
kilos = float(input("Ingrese el número de kilos: "))

if tipo in carnes:
    precio = carnes[tipo] * kilos
    print("Carne:", tipo)
    print("Total a pagar: $", format(precio, ",.0f"))
else:
    print("El tipo de carne no está.")