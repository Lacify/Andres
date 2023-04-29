# Lo primero que hacemos es usar el import para traer informacion del modulo aritmetico.

import output
import modulo_aritmetico

# Ahora utilizamos el while true para hacer un loop infinito solo siendo capaz de ser detenido por el usuario si es deseado, la variable "variable_usuario" 
# es la encargada de que el usuario determine lo que quiere hacer a continuacion y de que el usuario pueda salir del loop escribiendo la palabra salir
while(True):
    variable_usuario = input("Ingrese lo que desee hacer (suma, resta, multiplicacion, division, factorial o potencia): ")
    if variable_usuario == "salir":
        break
    # Aqui usamos n = int(input()) para que el input pase de ser str a int y se puedan ingresar numeros, luego creamos una lista vacia la cual con el append se ira llenando con la informacion
    # que el usuario brinde, siendo los numeros mencionados anteriormente, el resultado seria lo que se haga en el modulo aritmetico el cual ahi se explica como funciona.
    elif variable_usuario == "suma":
        n = int(input("ingrese la cantidad de numeros a utilizar: "))
        lista = []
        for i in range(n):
            a = int(input())
            lista.append(a)
        total = modulo_aritmetico.sumar(lista)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)
    # Aqui nada mas le pedimos al usuario que ingrese 2 numeros para restar entre si y el total es lo que haga la funcion denominada restar
    elif variable_usuario == "resta":
        a = int(input("ingrese el primer numero de la resta: "))
        b = int(input("ingrese el segundo numero de la resta: "))
        total = modulo_aritmetico.restar(a,b)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)
    # En esta hacemos exactamente lo mismo que en la de suma pero con la unica diferencia que extraemos el resultado de la funcion multiplicar y no la de sumar
    elif variable_usuario == "multiplicacion":
        n = int(input("ingrese la cantidad de numeros a utilizar: "))
        lista = []
        for i in range(n):
            a = int(input())
            lista.append(a)
        total = modulo_aritmetico.multiplicar(lista)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)
    # Esta es la unica distinta, aqui solo utilizamos un valor y ese valor una vez brindado por el usuario la funcion factorial le sacara el mismo factorial al numero.
    elif variable_usuario == "factorial":
        a = int(input("ingrese el numero para calcular el factorial: "))
        if a < 0:
            print("ERROR, No existen factoriales de numeros negativos, ingrese otro numero.")
            continue
        total = modulo_aritmetico.factorial(a)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)
    # Esta division es exactamente igual que la resta solo que la informacion sera sacadad de la funcion division y no de la funcion resta
    elif variable_usuario == "division":
        a = int(input("ingrese el primer numero de la division: "))
        b = int(input("ingrese el segundo numero de la division: "))
        if b == 0:
            print("ERROR, No se permite la division entre 0")
            continue 
        total = modulo_aritmetico.division(a,b)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)
    # Esta es exactamente igual a la resta y la suma, solo que saca la informacion de la funcion potencia y no de las otras funciones
    elif variable_usuario == "potencia":
        a = int(input("ingrese la base de la potencia: "))
        b = int(input("ingrese el exponente de la potencia: "))
        if a == 0 and b == 0:
            print("ERROR, No existe una potencia de 0 elevado a la 0")
            continue 
        total = modulo_aritmetico.potencia(a,b)
        print('Resultado: {}'.format(total))
        output.escribir_logs(variable_usuario.upper(), total)