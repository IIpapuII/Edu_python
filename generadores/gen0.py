def multiplosDe3(tope):
    num = 3
    miLista = []
    while num < tope:
        miLista.append(num)
        num = num+3
    return miLista

def suma_igual(rango,numero):
    suma = 0
    datos=0
    num=0
    dat1 =0 
    dat2 = 0
    while num< rango:
        dat1 = (num%10)
        dat2 = int((num/10)%10)
        suma = dat1 + dat2
        if(numero == suma ):
            yield num
        num= num+1

def multi_gen3(tope):
    num = 3
    while num < tope:
        yield num
        num = num+3


# multigen = multi_gen3(20)
# for i in multigen:
#     print(i)

# mul = multi_gen3(20)
# print(next(mul)) 
# print(next(mul))
