# esta funcion permite elevar  la potencia de dos numero de acuero a la entrada del usuario

def potencia():
    v = True
    while v:
        try:
            print("Esta funcion calcula la potencia de un numero")
            dat1 = int(input("Ingrese la base: "))
            dat2 = int(input("Ingrese el exponete: "))
            dato = dat1**dat2
            print("Resultado de la potencia: ", dato)
            v = False
        except:
            print("Se presento un erro al ingreso de datos")
            print("*******Ingrese un dato correctamente nuevamente*******")

potencia()