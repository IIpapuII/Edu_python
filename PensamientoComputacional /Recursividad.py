
def factorial(n):
    """Calcula el factorial de n.

    Args:
        n  int > 0: el valor de n debe ser mayor a cero
        return n! : retorna el factorial de n
    """
    if n == 1:
        return 1
    
    return n * factorial(n-1)
n = int(input('Escribre un entero :'))

print(factorial(n))