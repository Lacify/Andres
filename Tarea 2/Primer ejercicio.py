num = int(input("Ingresa un número entero positivo: "))
factorial = 1
#Aqui igualmente utilizamos el int para que el usuario pueda ingresar numeros enteros en vez de strings
if num <= 0:
    print("Numero Invalido, Por favor ingrese nuevamente otro numero")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es", factorial)
    
#aca condicionamos al num, si es menor o igual que 0 se pide que ingrese un valor distinto ya que numeros negativos o el mismo 0 no tienen factorial.
