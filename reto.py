class Estudiante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.notas = notas
        
    def calcular_definitiva(self):
        return calcular_definitiva(self.notas)
    
    def clasificar(self):
        definitiva = self.calcular_definitiva()
        return clasificar(definitiva)
    
def validar_nota(nota):
    return 0 <= nota <= 5

def calcular_definitiva(nota):
    return sum(nota)/len(nota)

def clasificar(definitiva):
    if definitiva == 5:
        return "Excelente"
    elif definitiva >= 4.5:
        return "Alto"
    elif definitiva >= 3:
        return "Basico"
    else:
        return "Bajo"
    
estudiante = []

while True:
    nombre = input("Nombre(fin para salir):")
    if nombre.lower()=="fin":
        break
    
    notas = []
    
    for i in range(3):
        nota = float(input(f"Ingrese Nota (i+1): "))
        
        if validar_nota(nota):
            notas.append(nota)
        else:
            print("Nota invalida")
    
    estudiante = Estudiante(nombre,notas)
    estudiante.append(estudiante)

for e in estudiantes:
    print("Nombre:", e.nombre)
    print("Definitiva:", e.calcular_definitiva())
    print("Clasificación:)", e.clasificar())
    print("-----")

#me falta cual es el mejor promedio y cuantos aprueban

