def multiplosDe3(tope):
    num = 3
    miLista = []
    while num < tope:
        miLista.append(num)
        num = num+3
    return miLista


def multi_gen3(tope):
    num = 3
    while num < tope:
        yield num
        num = num+3


multigen = multi_gen3(20)
for i in multigen:
    print(i)

mul = multi_gen3(20)
print(next(mul)) 
print(next(mul))
