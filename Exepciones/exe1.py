# esta funcion calcula la suma de los ultimos  tres digitos de  un numero

def suma_cifras():
    num = int(input("Ingrese un numero: "))
    result = num % 10
    result2 =int((num/10))%10
    result3  = int((num/10)/10)%10
    return(result+result2+result3)

try:
    print("Calculo de la suma de los ultimos digitos")
    dato = suma_cifras()
    print(dato)

except:
    print("El valor ingresado no corresponde a un numero ")
    print("********Intententalo nuevamente*********")
    print(dato = suma_cifras())