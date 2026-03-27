class Vehiculo():
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
     
    def info(self):
        super().info()  # Usa el método info() de Vehiculo
        print(f"Puertas: {self.puertas}")