#funciones que permiten el almacenado de diversas estruturas de datos.
def aplicar_operaciones(num):
    operaciones = [abs,float]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    return resultado

print(aplicar_operaciones(-2))