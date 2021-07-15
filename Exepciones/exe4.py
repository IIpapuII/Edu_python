#esta funcion calculo cuantos caracteres tiene un valor ingresado

def largo():
    suma = 0
    try:
        print("funcion calculo lo largo de una cadena de caracteres ")
        print("Ingrese la cadena a conercer su largo: ")
        dato  = input()
        caracter = list(dato)
        for i in caracter:
            suma = suma +1
        print("el largo de valor es: ",suma)
    except:
        print("Se presento un error en el caculo")

largo()