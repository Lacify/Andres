def eliminar_elementos_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

# Aqui simplemente hacemos que Python elimine elementos repetidos de la lista con el comando list(set que ya he usado en tareas anteriores.
lista = input("Ingrese la lista separada por comas: ").split(',')
# Le pedimos al usuario que ingrese la lista separada por comas para que al programa sea mas facil eliminar caracteres repetidos y sea mas entendible, por eso el split(,).
lista_sin_repetidos = eliminar_elementos_repetidos(lista)
# Y Aqui simplemente llamamos a la funcion, le denominamos lista_sin_repetidos y simplemente la imprimimos.
print(lista_sin_repetidos)