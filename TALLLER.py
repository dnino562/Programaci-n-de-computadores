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

class Medicamento():
    def __init__(self,nombre, requiere_formula, unidades, precio):
        self.__nombre = nombre
        self.__requiere_formula = requiere_formula
        self.__unidades = unidades
        self.__precio = precio

#Getters (encapsulamiento)
    def get_nombre(self): 			return self.__nombre
    def get_requiere_formula(self): return self.__requiere_formula
    def get_unidades(self): 		return self.__unidades
    def get_precio(self):           return self.__precio
    
    def __str__(self):
        formula = "Sí" if self._requiere_formula else "No"
        return (f"[Medicamento] {self.__nombre} | "
                f"[Fórmula: {formula} | "
                f"[Unidades: {self.__unidades} | "
                f"Precio: ${self.__precio:,.0f}")
    
   def vender(self, cantidad):
        if cantidad <= 0:
            print (f" Cantidad inválida para '{self.__nombre.}'.")
            return 0
        if cantidad > self.__unidades:
            print (f"No hay suficientes stock de '{self.__nombre}'."
                   f"Disponible: {self.__unidades}, solicitado: {cantidad}.")
            return 0

        self.__unidades -= cantidad
        total = cantidad * self.__precio
        print(f" Venta OK: {cantidad} unidad(es) de '{self.nombre}'"
              f "por ${total:,.0f}.")
        return total
        


class MedicamentoControlado(Medicamento):
    def __init__(self, nombre, requiere_formula, unidades, precio, dosis_maxima_diaria):
        super().__init__(nombre, requiere_formula, unidades, precio)
        self.dosis_maxima_diaria


    
    