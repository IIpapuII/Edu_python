# funcion retorna los digitos que son multiplos del rango

def multiplos_rango(rango):
    num = 1
    dat = rango
    while num < rango:
        dato = num % 100
        if dato == 0:
            dat = dat +1
        else:
            dat = rango % dato
        if (dat == 0):
            yield num
        num = num+1


salida = multiplos_rango(int(input("Ingrese el rango de numeros a comprobar: ")))
for i in salida:
    print("multiplos del rango : ", i)

print(104%100)