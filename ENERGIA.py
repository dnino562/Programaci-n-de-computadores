#9. clase SERVICIO e instancie un objeto llamado ENERGÍA.
class Servicio:
    nombre = "Energia"
    proveedor = "Electrificadora"
    costo = 80000
    tipo = "Publico"

    def activar(self):
        print(f"El servicio de {self.nombre} esta activo")

    def pagar(self):
        print(f"El servicio de {self.nombre} fue pagado")

ENERGIA = Servicio()
print(ENERGIA.nombre, ENERGIA.proveedor, ENERGIA.costo, ENERGIA.tipo)
ENERGIA.activar()
ENERGIA.pagar()