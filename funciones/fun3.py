arreglo = [1,2,3]
def suma_arreglo(arreglo):
    suma= 0
    for i in arreglo:
        suma = i + suma
    return suma

def main():
    total = suma_arreglo(arreglo)
    print("La suma del arreglo es : ",total)

if __name__ == "__main__":
    main()
