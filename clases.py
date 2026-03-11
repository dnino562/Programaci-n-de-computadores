class Personaje:
    def __init__(self, nombre, nivel=1, energia=100):
        self.nombre = nombre
        self.nivel = nivel
        self.energia = energia

    def atacar(self):
        self.energia = -10
        print(f"{self.nombre} atacar. Energía restante: {self.energia}")

    def descansar(self):
        self.energia = 100
        print(f"{self.nombre} descansa. Energía restaurada a {self.energia}")

    def mostrar_estado(self):
        print("Estado de Personaje")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Energía: {self.energia}")
    
    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} subió de nivel. Nuevo nivel: {self.nivel}")
