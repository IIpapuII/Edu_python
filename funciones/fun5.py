# esta funcion retorna el promedio de los datos pares
Arreglo = [1, 2, 3, 4]


def promedio_pares(arreglo):
    pares = 0
    for i in arreglo:
        i % 2
        if (i % 2) == 0:
            pares = pares + i
    promedio = pares / len(arreglo)
    print("El promedio de los datos pares es :", promedio)

promedio_pares(Arreglo)
