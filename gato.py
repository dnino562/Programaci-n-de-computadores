#1. clase ANIMAL e instancie un objeto llamado GATO.
class Animal:
    especie = "Felino"
    color = "Negro"
    edad = 3
    peso = 4

    def comer(self):
        print(f"El {self.especie} está comiendo")

    def dormir(self):
        print(f"El {self.especie} está durmiendo")

GATO = Animal()
print(GATO.especie, GATO.color, GATO.edad, GATO.peso)
GATO.comer()
GATO.dormir()