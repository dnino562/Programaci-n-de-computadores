#TALLER: La drogueria de don Misael
#DIAGRAMA DE CLASES (paso obgligatorio antes de codificar)

#Clase:Medicamento
#  atributos:nombre(str),requiere_formula(bool),
#            unidades(int),precio(float)
#  métodos: __init__, __str__, vender (cantidad)

#Clase: MedicamentoControlado(Medicamento)
# atributo extra: dosis_maxima_diaria(str)
# métodos: __init__(con super()).__str__(sobreescrito)

#Funciones Generales:
# guardar_inventario(lista, archivo) -> None
# cargar_inventario(archivo)  -> lista

class Medicamento:
    def __init__(self, nombre, requiere_formula, unidades, precio):
        self.__nombre = nombre
        self.__requiere_formula = requiere_formula
        self.__unidades = unidades
        self.__precio = precio

    # Getters
    def get_nombre(self): return self.__nombre
    def get_requiere_formula(self): return self.__requiere_formula
    def get_unidades(self): return self.__unidades
    def get_precio(self): return self.__precio
    
    def __str__(self):
        formula = "Sí" if self.__requiere_formula else "No"
        return (f"[Medicamento] {self.__nombre} | "
                f"Fórmula: {formula} | "
                f"Unidades: {self.__unidades} | "
                f"Precio: ${self.__precio:,.0f}")

    def vender(self, cantidad):
        if cantidad <= 0:
            print(f"Cantidad inválida para '{self.__nombre}'.")
            return 0

        if cantidad > self.__unidades:
            print(f"No hay suficiente stock de '{self.__nombre}'. "
                  f"Disponible: {self.__unidades}, solicitado: {cantidad}.")
            return 0

        self.__unidades -= cantidad
        total = cantidad * self.__precio
        print(f"Venta OK: {cantidad} unidad(es) de '{self.__nombre}' "
              f"por ${total:,.0f}.")
        return total


class MedicamentoControlado(Medicamento):
    def __init__(self, nombre, requiere_formula, unidades, precio, dosis_maxima_diaria):
        super().__init__(nombre, requiere_formula, unidades, precio)
        self.__dosis_maxima_diaria = dosis_maxima_diaria

    def __str__(self):
        return super().__str__() + \
               f" | Dosis máxima diaria: {self.__dosis_maxima_diaria}"
    
def guardar_inventario(lista, archivo):
    with open(archivo, "w") as f:
        for med in lista:
            if isinstance(med, MedicamentoControlado):
                f.write(f"C,{med.get_nombre()},{med.get_requiere_formula()},"
                        f"{med.get_unidades()},{med.get_precio()},"
                        f"{med._MedicamentoControlado__dosis_maxima_diaria}\n")
            else:
                f.write(f"N,{med.get_nombre()},{med.get_requiere_formula()},"
                        f"{med.get_unidades()},{med.get_precio()}\n")

def cargar_inventario(archivo):
    inventario = []
    try:
        with open(archivo, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")

                if datos[0] == "C":
                    _, nombre, formula, unidades, precio, dosis = datos
                    inventario.append(
                        MedicamentoControlado(nombre,formula == "True",
                            int(unidades),
                            float(precio),
                            dosis))
                else:
                    _, nombre, formula, unidades, precio = datos
                    inventario.append(
                        Medicamento(nombre,formula == "True",
                            int(unidades),
                            float(precio)))
    except FileNotFoundError:
        print("Inventario nuevo creado.")

    return inventario
inventario = cargar_inventario("inventario.txt")

if not inventario:
    inventario.append(Medicamento("Aspirina", False, 20, 1500))
    inventario.append(Medicamento("Jarabe", False, 15, 8000))
    inventario.append(MedicamentoControlado("Tramadol", True, 10, 5000, "2 tabletas"))
    inventario.append(MedicamentoControlado("Morfina", True, 5, 12000, "1 ampolla"))

recaudo = 0
recaudo += inventario[0].vender(3)
recaudo += inventario[1].vender(2)
recaudo += inventario[2].vender(1)
recaudo += inventario[3].vender(1)

print("\nRecaudo total del día: $", recaudo)

print("\nMedicamentos por agotarse:")
for med in inventario:
    if med.get_unidades() <= 5:
        print(med)

guardar_inventario(inventario, "inventario.txt")