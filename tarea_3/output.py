# Esta función se escarga de escribir los resultados de las operaciones en un log.
def escribir_logs(operacion,total):
    file = open("resultados.log", "a")
    file.write("Operacion: {}, Resultado: {}\n".format(operacion, total))
    file.close()