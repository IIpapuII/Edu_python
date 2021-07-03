#funcion que permmite retornar el promedio de una lista de arreglos
Arreglo = [1,2,3,4,5,6,7]
def Promedio_lista(arreglo):
    dato =0
    for i in arreglo:
        dato = dato + i
    promedio = dato / len(arreglo)
    print("El promedio del arreglo es: ",promedio)

Promedio_lista(Arreglo)
