class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return self.titulo + " - " + self.autor
    
    
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        
    def agregar(self, titulo, autor):
        self.libros.append(Libro(titulo, autor))

    def listar(self):
        if not self.libros:
            print("No hay libros")
        else:
        # Recorre la lista de libros con un for
            for libro in self.libros:
                print(libro) # se usa __str__ de Libro
    
    
    # Guardar libros en un archivo de texto
    def guardar(self, archivo):
        with open(archivo, "w") as f:
            #"w" = write → crea archivo si no existe
            # sobrescribe todo lo que haya dentro si ya existe
            for libro in self.libros:
                f.write(f"{libro.titulo},{libro.autor}\n")

    def cargar(self, archivo):
        # Vacía la lista de libros antes de cargar los nuevos
        self.libros = []
        try:
            # Abre el archivo en modo lectura ("r")
            # "r" = read → solo lectura, el archivo debe existir
            with open(archivo, "r") as f:
                # Recorre cada línea del archivo
                for linea in f:
                    titulo, autor = linea.strip().split(",")
                    # Crea un objeto Libro con los datos y lo agrega a la lista
                    self.libros.append(Libro(titulo, autor))
        except FileNotFoundError:
            print("El archivo no existe.")
