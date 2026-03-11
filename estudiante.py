class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre #atributo privado
        self._nota = nota # atributo privado
    
    def get_nota(self):
        return self._nota
    
    def set_nota(self, nueva_nota):
        if 0 <= nueva_nota <=5:
            self._nota = nueva_nota
        else:
            print("Nota inválida")

obj = Estudiante("Danna", 5)
print(obj.get_nota())
obj.set_nota(-1)
print(obj.get_nota())
obj._nota = 10
print(obj.get_nota())