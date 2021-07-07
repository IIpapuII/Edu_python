# fuuncion compara el primer y el ultimo digito

def comparar_digitos(rango):
    num = 1
    while num < rango:
        dig1 = str(num)
        dig1 = int(dig1[0])
        dig2 = num % 10
        if (dig1 == dig2):
            yield num
        num = num + 1


salida = comparar_digitos(
    int(input("Ingrese el rango de numeros a comparar: ")))

for i in salida:
    print("Salida de numeros iguales: ", i)
