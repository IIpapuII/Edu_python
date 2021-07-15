#Esta funcion cuenta las vocales de un strig

def cuenta_vocales():
    suma = 0
    try:
        print("Ingrese el string a validar")
        valor = list(input())
        print(valor)
        for i in valor:
            if i == 'a':
                suma = suma+ 1
            elif i == 'e':
                suma = suma + 1
            elif i == 'i':
                suma = suma +1
            elif i == 'o':
                suma = suma +1
            elif i == 'u':
                suma = suma +1
            else:
                continue
        print("Cantidad de vocales: ", suma)
    except: 
        print("Se presento un error durante la ejecucion")   

cuenta_vocales()