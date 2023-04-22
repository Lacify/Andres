import random

notas = {
    "Matematicas": random.randint(0, 100),
    "Ciencias": random.randint(0, 100),
    "Ingles": random.randint(0, 100),
    "Informatica": random.randint(0, 100)
}
#Aqui utilizamos nuevamente el random.randit para que nos genere caracteres al azar esta vez entre 0 y 100 como puede ser una calificacion en la vida real
promedio = sum(notas.values()) / len(notas)
#Para sacar el promedio hacemos la operacion correspondiente para sacar el promedio anual de notas con el cual se definiria si el estudiante pasa el curso o no
promedio_anual = {"Estudiante": "Andres", "Promedio Anual": promedio}
#Ahora al resultado total le llamamos promedio_anual, ingresamos la informacion del estudiante en este caso el nombre y el promedio general/anual

print(promedio_anual)
print(notas)
#Terminamos imprimiendo el promedio anual antes calculado junto con el nombre del estudiante y tambien imprimimos las notas de cada materia por separado