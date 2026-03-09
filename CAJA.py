#10. clase EMPAQUE e instancie un objeto llamado CAJA.
class Empaque:
    tipo = "Caja"
    material = "Carton"
    tamaño = "Grande"
    peso = "Ligero"

    def abrir(self):
        print(f"La {self.tipo} se abre")

    def cerrar(self):
        print(f"La {self.tipo} se cierra")

CAJA = Empaque()
print(CAJA.tipo, CAJA.material, CAJA.tamaño, CAJA.peso)
CAJA.abrir()
CAJA.cerrar()