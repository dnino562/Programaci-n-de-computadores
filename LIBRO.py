#6. clase LIBRO e instancie un objeto llamado NOVELA
class Libro:
    titulo = "Cien años de soledad"
    autor = "Gabriel Garcia Marquez"
    paginas = 417
    genero = "Novela"

    def abrir(self):
        print(f"El libro {self.titulo} se abre")

    def cerrar(self):
        print(f"El libro {self.titulo} se cierra")

NOVELA = Libro()
print(NOVELA.titulo, NOVELA.autor, NOVELA.paginas, NOVELA.genero)
NOVELA.abrir()
NOVELA.cerrar()