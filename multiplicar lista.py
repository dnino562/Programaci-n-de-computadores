def multiplicar_lista(lista, numero):
    nueva_lista = []
    
    for i in lista:
        nueva_lista.append(i * numero)
        
    return nueva_lista

print(multiplicar_lista([1,2,3], 2))