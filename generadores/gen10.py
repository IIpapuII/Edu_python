# esta funcion compara si el primir digito es multiplo del ultimo

def comparacion_multiplos(rango):
    num =1
    while num  < rango:
        dig1 = str(num)
        dig1 = int(dig1[0])
        dig2 = num %10
        if(0 ==(dig2%dig1)):
            yield num
        num = num+1

salidad = comparacion_multiplos(int(input("Ingrese el rango de  numeros a comparar: ")))

for i in salidad:
    print("numeros multiplos: ",i)
