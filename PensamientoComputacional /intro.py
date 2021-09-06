def contador_simple():
    contador = 0
    while contador < 10:
        print(contador)
        contador += 1  # esto es lo mismo  que contador = contador + 1


def new_func():
    contador_externo = 0
    contador_interno = 0
# funcionamiento en forma de relog
    while contador_externo < 5:
        while contador_interno < 6:
            print(contador_externo, contador_interno)
            contador_interno += 1
        contador_externo += 1
        contador_interno = 0

def new_funtion_if():
    contador_externo =0
    contador_interno=0
    while contador_externo < 5:
        while contador_interno < 6:
            print(contador_externo,contador_interno)
            contador_interno += 1
            if contador_interno >= 3:
                break
        contador_externo += 1
        contador_interno =0

new_funtion_if()


