num = int(input("Ingrese un numero positivo: "))
#aca utilizamos el int para que el input en vez de ser una string sea un numero entero
if num <= 0:
    print("Favor ingresar un numero mayor a 0")
else:
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
        
#En este codigo le ponemos un if al primero, si "num" es un valor igual o menos a 0 tirara un error pero de lo contrario ejecutara el codigo correspondiente sin problema alguno
#al num le sumamos un 1 para que asi la cuenta sea mas "humana" ya que no empezaria desde 0 si no desde el 1