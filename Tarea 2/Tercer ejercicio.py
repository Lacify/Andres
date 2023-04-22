str1 = input("Ingresa la primera string: ")
str2 = input("Ingresa la segunda string: ")
#utilizamos el comando input para colocar un enunciado que nos permita darle a entender al usuario lo que tiene que ingresar y a continuacion lo ingrese
if len(str1) != len(str2):
    print("ERROR, Favor ingresar strings con la misma longitud.")
else:
    str_intercalada = ""
    for i in range(len(str1)):
        str_intercalada += str1[i] + str2[i]
    print(str_intercalada)
    
#Aqui se utilizo la funcion len para determinar la longitud de la string introducida por el usuario y saber si tienen una longitud de caracteres similar
#Posteriormente utilizamos el if y else para ambos posibles casos, en caso de que el usuario introduzca strings de distintas longitudes el programa le dara un mensaje de error
#Y en caso de que introduzca strings de longitudes iguales, Python ignorara por completo el codigo del If y utilizara el codigo del Else como si el If no existiera
