# esta funcion retorna la suma de los ultimos digitos se igual a 4

def suma_igual_4(rango):
    suma = 0
    datos=0
    num=0
    dat1 =0 
    dat2 = 0
    while num< rango:
        dat1 = (num%10)
        dat2 = int((num/10)%10)
        suma = dat1 + dat2
        if(4 == suma ):
            datos = num
            yield datos
        num= num+1

salida = suma_igual_4(int(input("Ingrese el rango de numeros: ")))
for i in salida:
    print("los numeros que suman 4 son: ",i)

