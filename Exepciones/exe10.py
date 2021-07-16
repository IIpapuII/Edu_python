#determinar si dos numeros enteros tiene la misma cantidad de digitos

def comparar_digitos():
    suma1 = 0
    suma2 =0 
    try:
        print("ingrese el primer numero ")
        num1 = int(input())
        print("Ingrese el segundo numero")
        num2 = int(input())
        num1 = str(num1)
        num2 = str(num2)
        for i in range(len(num1)):
            suma1 = suma1 +1
        for a in range(len(num2)):
            suma2 = suma2 + 1
        if suma1 == suma2:
            print("los numeros tiene la misma cantidad de digitos")
        else:
            print("los numero tienes cantidad diferente de digitos")
    except:
        print("se presenta un error en el tipo de dato ingresado")

comparar_digitos()