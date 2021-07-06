# funcion genera los multiplos de  4

def multiplo_de_4(rango):
    num = 4
    while num < rango:
        yield num
        num = num + 4


multi = multiplo_de_4(int(input("Ingrese el rango: ")))
for i in multi:
    print("multiplo de 4: ", i)
