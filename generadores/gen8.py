#la  funcion muestra de tal numero a tal dados por el usuario un contador de rangos

def rango(num1,num2):
        num = num1
        while num < num2:
            yield num
            num = num +1

dat1 = int(input("Ingrese numero de inicio: "))
dat2 = int(input("Igrese el rango final: "))
salida = rango(dat1,dat2)
for i in salida:
    print("El rango de numero es el siguiente: ",i)