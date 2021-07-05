# esta funcion devuelve si el  ultimo valor de un numero correponde a n valor de  n numero

def com_final_valor(valor,com):
    ultimo = valor %  10
    if( ultimo == com):
        print("El ultimo valor es",com," esta en :",valor)
    else:
        print("El ultimo valor ",com," es diferente al de la sifra",ultimo)
    

com_final_valor(1234,4)
