# programa muetra los numeros de 2 digitos que son impares

def dos_impar(rango):
    num = 1
    while num < rango:
        if num > 10 and num < 100:
            if (num%2)!= 0:
                yield num
        num = num + 1

salida = dos_impar(int(input("Ingrese el rango a comprobar: ")))
for i in salida:
    print("Numeros impares de dos digitos: ",i)

            


