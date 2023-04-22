Lista_con_duplicados = [1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 2 ,0 ,7, 7, 6, 6, 0, 9, 9, 1, 8, 8]

Segunda_lista_con_duplicados = [7, 7, 7, 7, 7, 7, 7, 7, 7]

Lista_sin_duplicados = list(set(Lista_con_duplicados))
#Aca utilizamos el comando list(set para que a la hora de identificar la lista "Lista_con_duplicados" detecte cada elemento y lo vuelva unico en cada lista seleccionada.
Segunda_lista_sin_duplicados = list(set(Segunda_lista_con_duplicados))
#Aqui hacemos lo mismo pero con una lista distinta para ver distintos resultados.
print("Lista de Duplicados")
print('\n', Lista_con_duplicados, '\n')
print("Lista de No Duplicados")
print('\n', Lista_sin_duplicados, '\n')
print("Segunda lista de Duplicados")
print('\n',Segunda_lista_con_duplicados, '\n')
print("Segunda lista de No Duplicados")
print('\n',Segunda_lista_sin_duplicados, '\n')
#A la hora de imprimir lo que decidi implementar es el '\n' al rededor de lo que se imprimira solo para que haya un espaciado entre cada print y quede mucho mas legible y estetico
#al igual que puse un print con nombres de cada lista para que se entienda de que es cada cosa