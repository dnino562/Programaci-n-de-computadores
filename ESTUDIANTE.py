#11. clase PERSONA e instancie un objeto llamado ESTUDIANTE
class Persona:
    nombre = "Ana"
    edad = 18
    ciudad = "Bucaramanga"
    ocupacion = "Estudiante"

    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

    def descansar(self):
        print(f"{self.nombre} esta descansando")

ESTUDIANTE = Persona()
print(ESTUDIANTE.nombre, ESTUDIANTE.edad, ESTUDIANTE.ciudad, ESTUDIANTE.ocupacion)
ESTUDIANTE.estudiar()
ESTUDIANTE.descansar()