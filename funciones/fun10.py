# esta funcion retorna la cantidad de n numeros iguales es la ultima cifra de un arreglo de numeros
def com_cifra_arreglos(valor, n):
    suma = 0
    for i in valor:
        if (i%10)== n:
            suma = suma +1
    print("cantiad de datos que terminan en ",n," del arreglo: ",suma)
arreglo = [123,4567,23234,65464]
 
com_cifra_arreglos(arreglo,4)