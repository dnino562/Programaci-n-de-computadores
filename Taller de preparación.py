# 1 y 5 Clase EMPAQUE → objetos: CAJA y BOLSA
class Empaque:
    def __init__(self, material, peso, capacidad):
        self.material = material
        self.__peso = peso  # atributo privado
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Material: {self.material}, Peso: {self.__peso}, Capacidad: {self.capacidad}")

    def cambiar_peso(self, nuevo_peso):
        self.__peso = nuevo_peso


# Herencia
class Caja(Empaque):
    def abrir(self):
        print("La caja ha sido abierta")

class Bolsa(Empaque):
    def cerrar(self):
        print("La bolsa ha sido cerrada")


# Objetos
caja = Caja("Cartón", 2, "10kg")
bolsa = Bolsa("Plástico", 1, "5kg")

# 2 y 3 Clase VEHICULO → objetos: MOTO y CARRO
class Vehiculo:
    def __init__(self, marca, velocidad, combustible):
        self.marca = marca
        self.__velocidad = velocidad  # privado
        self.combustible = combustible

    def acelerar(self):
        print("El vehículo está acelerando")

    def obtener_velocidad(self):
        return self.__velocidad


# Herencia
class Moto(Vehiculo):
    def hacer_caballito(self):
        print("La moto hace caballito")

class Carro(Vehiculo):
    def encender_radio(self):
        print("El carro encendió el radio")


# Objetos
moto = Moto("Yamaha", 120, "Gasolina")
carro = Carro("Toyota", 180, "Gasolina")

#4 Clase ARBOL → objeto: PINO
class Arbol:
    def __init__(self, altura, edad, tipo):
        self.altura = altura
        self.__edad = edad  # privado
        self.tipo = tipo

    def crecer(self):
        print("El árbol está creciendo")

    def obtener_edad(self):
        return self.__edad


# Herencia
class Pino(Arbol):
    def producir_pinas(self):
        print("El pino produce piñas")


# Objeto
pino = Pino(5, 10, "Conífera")

