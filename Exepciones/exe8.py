# buscar caracter digitada por el usuario
def consulta_caracter():

    suma = 0
    try:
        print("Ingrese la cadena de palabras de palabras")
        valor = input()
        print("ingrese el caracter a buscar")
        valor2 = ord(input())
        valor2 = chr(valor2)
        dato = list(valor)
        for i in dato:
            if i == valor2:
                suma = suma + 1
            else:
                continue
        print("los caracteres encontrados son: ", suma)
    except:
        print("se presento un error al ingresar datos vuelve a intentarlo")
        consulta_caracter()


consulta_caracter()
