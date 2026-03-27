class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        # debe devolver "Hola, soy <nombre> y tengo <edad> años"
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")