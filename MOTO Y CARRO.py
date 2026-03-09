#2. clase VEHICULO e instancie un objeto llamado MOTO.
#3. clase VEHÍCULO e instancie un objeto llamado CARRO
class Vehiculo:
    marca = ""
    modelo = ""
    año = 0
    color = ""

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} acelera")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} frena")

MOTO = Vehiculo()
MOTO.marca = "Yamaha"
MOTO.modelo = "FZ"
MOTO.año = 2022
MOTO.color = "Azul"

CARRO = Vehiculo()
CARRO.marca = "Toyota"
CARRO.modelo = "Corolla"
CARRO.año = 2021
CARRO.color = "Blanco"

print(MOTO.marca, MOTO.modelo, MOTO.año, MOTO.color)
print(CARRO.marca, CARRO.modelo, CARRO.año, CARRO.color)
MOTO.acelerar()
CARRO.frenar()