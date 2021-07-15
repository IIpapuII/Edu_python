# esta funcion permmite resolver la raiz cuadrada de un numero
import math


def raiz():
    valor = True
    while valor:
        try:
            print("Esta funcion calcula la raiz cuadra de un numero")
            dato = int(input("Ingrese el valor a evaluar: "))
            salida = math.sqrt(dato)
            print("El resultado de la raiz es: ",salida)
            valor = False
        except:
            print("Se genero un error por valor incorrecto ingresado o raiz indefinida")
            print("************Ingrese nuevamente el numero  a comprobar***************")

raiz()