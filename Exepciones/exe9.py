# esta funcion divide a un numero entre 4
def divirdir():
    try:
        print("Ingrese un numero para dividir enntre 4")
        num = int(input())
        print("resultado:",num/4)
    except:
        print("El numero ingresado no se puede divirdir entre 4")
        divirdir()

divirdir()