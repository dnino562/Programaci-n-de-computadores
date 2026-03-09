#4. clase COMIDA e instancie un objeto llamado BANDEJA PAISA.
class Comida:
    nombre = "Bandeja Paisa"
    origen = "Colombia"
    calorias = 1200
    precio = 25000

    def servir(self):
        print(f"La {self.nombre} está servida")

    def comer(self):
        print(f"La {self.nombre} está siendo comida")

BANDEJA_PAISA = Comida()
print(BANDEJA_PAISA.nombre, BANDEJA_PAISA.origen, BANDEJA_PAISA.calorias, BANDEJA_PAISA.precio)
BANDEJA_PAISA.servir()
BANDEJA_PAISA.comer()