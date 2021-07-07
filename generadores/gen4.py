#esta funcion muentra que numeros son iguales del ultimo y penultimo digito 

def iguales_ultimos(rango):
    dat1 = 0
    dat2 = 0
    num =1
    while num < rango:
        dat1 = num %10
        dat2 = int((num/10)%10)
        if (dat1 == dat2):
            yield num
        num = num +1

salida = iguales_ultimos(int(input("Ingrese el rango de numeros: ")))
for i in salida:
    print("numeros iguales de cifras finales : ", i)
