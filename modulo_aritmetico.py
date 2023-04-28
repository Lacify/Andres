#Utilizamos el def para definir una funcion la cual en este caso nombramos sumar y le brindamos el valor lista, luego utilizamos el for i in range len lista para darle a entender a 
#Python que la suma que hara no debe sobrepasar los limites de la lista dada por el usuario, luego hacemos la suma del total con la lista, cada vez que se ingrese un digito en la 
#lista el total cambiara inicia como un 0, si primer caracter de la lista es 1 ahora el total pasa de 0 a 1, si el siguiente caracter de la lista es 3 ahora se hace el 1 + 3 
#quedando total en un 4 y asi
def sumar(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    return total
#Aqui es mucho mas simple, solamente definimos la funcion restar, le brindamos el valo a,b y dentro de la funcion hacemos la resta de caracteres siendo C el resultado de la resta
def restar(a,b):
    c = a - b
    return c
#Aqui hacemos lo mismo que en la de la suma solamente que le cambiamos el + por un * y en vez de que el valor de total sea 0 se volvera 1 ya que si fuera 0 cancelaria todo
def multiplicar(lista):
    total = 1
    for i in range(len(lista)):
        total = total * lista[i]
    return total
#Aqui igual que la resta solamente sustituimos el - con un / para dividir
def division(a,b):
    c = a / b
    return c
#Aqui hacemos el proceso debido de un factorial, le damos un solo valor ya que solo se sacara el factorial a un solo digito, posteriormente hacemos el for i in range para que
#entienda que el factorial debe llegar desde 1 hasta el valor de a + 1 que seria lo que brinde el usuario + 1 para que la cuenta no empiece de 0
def factorial(a):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial
#Por ultimo aqui hacemos lo mismo que en la resta y la division solo que sistuimos por ** para que se haga la potencia entre los valores que de el usuario
def potencia(a,b):
    c = a ** b
    return c