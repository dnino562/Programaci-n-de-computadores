def palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = input("Ingrese una palabra: ")
print(palindromo(palabra))