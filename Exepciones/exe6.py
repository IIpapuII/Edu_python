#funcion cuenta palabras 

from typing import List


def cuenta_palabras():
    suma = 0
    try:
        print("Ingrese la cadena de string")
        valor = input()
        dato = list(valor)
        for i in dato:
            if i == ' ':
                suma = suma + 1
            else:
                continue
    
    except:
        print("se presento un error durante la ejecucion")
    print("La cantidad de palabras: ",suma+1)

cuenta_palabras()