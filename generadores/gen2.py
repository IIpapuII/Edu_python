# esta funcion genera y muestra todos los numeros terminados en 3

def final_a_3(rango):
    num = 1
    numal = 0

    while num < rango:
        if(3 == (num % 10)):
            numal = num
            yield numal
        num = num + 1


salida = final_a_3(int(input("Ingrese el rango de numeros: ")))
for i in salida:
    print(i)

