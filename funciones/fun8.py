#esta funcion debuelve la tabla de multiplicar de un valor

def tabla_multiplicar(valor):
    for i in range (1,11):
        mul = i * valor
        print(i,"X",valor, " = ", mul)

tabla_multiplicar(6)