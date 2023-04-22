import random
#Colocamos random.randint para que python nos genere numeros al azar entre las barreras que le pongamos, en este caso del 1 al 200
lista = [random.randint(1, 200) for _ in range(random.randint(1, 200))] 

print("Lista inicial:")
print(lista)
#para generar la lista de los cubos ponemos ** para hacer la potencia de "num" en la lista inicial
lista_cubos = [num ** 3 for num in lista]

print("Lista de numeros al cubo:")
print(lista_cubos)

