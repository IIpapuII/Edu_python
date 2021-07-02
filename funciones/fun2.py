n = int(input("Ingrese  la cantidad de veces a imprimir: "))
nombre = input(str("Ingrese su nombre: "))

def ImprimirNombres(nombre,n):
    for i in range(n):
        print(nombre)

def main():
    ImprimirNombres(nombre, n)

if __name__ == "__main__":
    main()
