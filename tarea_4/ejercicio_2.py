def contar_apariciones(cadena):
    contador = {}
    for caracter in cadena:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    return contador
# Aqui basicamente le indicamos a Python que cada caracter encontrado en contador debe ser contado por cada aparicion empezando desde el uno, por eso el +1.
cadena = input("Introduce los caracteres deseados: ")
resultado = contar_apariciones(cadena)
print(resultado)
# Luego nada mas le decimos a Python que resultado es igual a toda la funcion contar_apariciones e imprimimos resultado.