def escribir_logs(operacion,total):
    file = open("resultados.log", "a")
    file.write("Operacion: {}, Resultado: {}\n".format(operacion, total))
    file.close()