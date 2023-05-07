def convertir_lista_y_tupla(secuencia):
    numeros = secuencia.split(',')
    lista = list(map(int, numeros))
    tupla = tuple(map(int, numeros))
    return lista, tupla
# aca utilizamos map(int, numeros) para convertir cada cadena de texto en un número entero, esto se aplica tanto para la lista como para la tupla.
secuencia = input("Ingrese una secuencia de numeros separados por comas: ")
# Aca le pedimos al usuario que ingrese los numeros para crear la lista y la tupla
resultado_lista, resultado_tupla = convertir_lista_y_tupla(secuencia)
# Aca por ultimo llamamos a la funcion y la nombramos tanto resultado_lista como resultado_tupla
print("Lista:", resultado_lista)
print("Tupla:", resultado_tupla)
# Por ultimo imprimimos la lista y la tupla