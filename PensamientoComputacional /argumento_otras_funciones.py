def multiplicar_por_dos(n):
    return n*2

def sumar_dos(n):
    return n+2

def aplicar_operaciones(f, numeros):
    resultados = []
    for numero in numeros:
        resultados = f(numero)
        resultados.append(resultados)

#funciones en forma de lambda o redusidas 
sumar = lambda x,y:x+y
print(sumar(5,6))

