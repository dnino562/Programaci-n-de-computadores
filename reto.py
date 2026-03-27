class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        
    def calcular_definitiva(self):
        return sum(self.notas) / len(self.notas)
    
    def clasificar(self):
        definitiva = self.calcular_definitiva()
        if definitiva == 5:
            return "Excelente"
        elif definitiva >= 4.5:
            return "Alto"
        elif definitiva >= 3:
            return "Basico"
        else:
            return "Bajo"


def validar_nota(nota):
    return 0 <= nota <= 5


# LISTA correcta
estudiantes = []

while True:
    nombre = input("Nombre (fin para salir): ")
    if nombre.lower() == "fin":
        break
    
    notas = []
    
    for i in range(3):
        while True:
            nota = float(input(f"Ingrese Nota {i+1}: "))
            if validar_nota(nota):
                notas.append(nota)
                break
            else:
                print("Nota inválida, intente de nuevo.")
    
    estudiante = Estudiante(nombre, notas)
    estudiantes.append(estudiante)


# Mostrar resultados
mejor_promedio = 0
mejor_estudiante = ""
aprobados = 0

for e in estudiantes:
    definitiva = e.calcular_definitiva()
    print("Nombre:", e.nombre)
    print("Definitiva:", definitiva)
    print("Clasificación:", e.clasificar())
    print("-----")
    
    # Mejor promedio
    if definitiva > mejor_promedio:
        mejor_promedio = definitiva
        mejor_estudiante = e.nombre
    
    # Aprobados (>=3)
    if definitiva >= 3:
        aprobados += 1


print("Mejor promedio:", mejor_estudiante, "-", mejor_promedio)
print("Cantidad de aprobados:", aprobados)