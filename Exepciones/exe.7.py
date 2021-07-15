#esta funcion cuenta las cadenas de caracteres todas las letras a

def letras_a():
    suma = 0
    try:
        print("Ingrese la cadena de caracteres a comprobar: ")
        valor = str(input())
        dato = list(valor)
        for i in dato:
            if i == 'A':
                suma = suma+1
            elif i == 'a':
                suma = suma + 1
            else:
                continue
    except:
        print("se presento algun error")
        letras_a()
    print("La cantidad de letras a es : ", suma)

letras_a()
