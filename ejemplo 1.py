diccionario = {"amor": "Sentimiento intenso del ser humano que, partiendo de su propia insuficiencia, necesita y busca el encuentro y unión con otro ser.",
"libro": "Conjunto de muchas hojas de papel u otro material semejante que, encuadernadas, forman un volumen.",
"computadora": "Máquina electrónica capaz de almacenar información y tratarla automáticamente mediante operaciones matemáticas y lógicas.",
"amistad": "Afecto personal, puro y desinteresado, compartido con otra persona.",
"familia": "Grupo de personas emparentadas entre sí que viven juntas."}


palabra = input("Ingrese una palabra: ")


if palabra in diccionario:
    print("Definición:", diccionario[palabra])
else:
    print("La palabra no se encuentra en el diccionario.")