caracteres = input("Ingrese los caracteres deseados: ")
# Introducimos aqui un input para que el usuario ingrese los caracteres que quiera que python cuente y le nombramos caracteres.
letras = 0
numeros = 0
caracteres_especiales = 0
# Aqui le asignamos un valor numerico (en este caso 0) a cada una de las opciones lo cual luego cambiara dependiendo de lo que haya ingresado el usuario.

for caracter in caracteres:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:
            caracteres_especiales += 1

"""""""""""
Ponemos el isalpha para que python determine si es un valor alfabetico, de serlo contara cada caracter y te nombrara cuantos hay apartir del 1, por eso el +1
pasa lo mismo con el isdigit, detectara si son numeros y empezara a contarlos.
"""
print("Letras =", letras)
print("Numeros =", numeros)
print("Caracteres especiales =", caracteres_especiales)
# Para finalizar usamos un print para que se muestre en la terminal todos los resultados de los codigos anteriores.