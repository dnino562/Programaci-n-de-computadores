#8. clase DISPOSITIVO e instancie un objeto llamado PORTATIL.

class Dispositivo:
    marca = "HP"
    tipo = "Portatil"
    ram = "16GB"
    almacenamiento = "1TB"

    def encender(self):
        print(f"El {self.tipo} {self.marca} se enciende")

    def apagar(self):
        print(f"El {self.tipo} {self.marca} se apaga")

PORTATIL = Dispositivo()
print(PORTATIL.marca, PORTATIL.tipo, PORTATIL.ram, PORTATIL.almacenamiento)
PORTATIL.encender()
PORTATIL.apagar()