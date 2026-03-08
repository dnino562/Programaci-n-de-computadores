nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

usuario = {"nombre": nombre,"edad": edad,"direccion": direccion,"telefono": telefono}


print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}")