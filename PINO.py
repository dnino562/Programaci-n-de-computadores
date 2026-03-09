#5. clase ARBOL e instancie un objeto llamado PINO.
class Arbol:
    tipo = "Pino"
    altura = 10
    color = "Verde"
    edad = 5

    def crecer(self):
        print(f"El {self.tipo} está creciendo")

    def oxigeno(self):
        print(f"El {self.tipo} produce oxígeno")

PINO = Arbol()
print(PINO.tipo, PINO.altura, PINO.color, PINO.edad)
PINO.crecer()
PINO.oxigeno()