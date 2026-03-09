#7. clase PELICULA e instancie un objeto llamado MONSTERSINC.
class Pelicula:
    titulo = "Monsters Inc"
    genero = "Animacion"
    duracion = 92
    anio = 2001

    def reproducir(self):
        print(f"La pelicula {self.titulo} se reproduce")

    def pausar(self):
        print(f"La pelicula {self.titulo} se pausa")

MONSTERSINC = Pelicula()
print(MONSTERSINC.titulo, MONSTERSINC.genero, MONSTERSINC.duracion, MONSTERSINC.anio)
MONSTERSINC.reproducir()
MONSTERSINC.pausar()