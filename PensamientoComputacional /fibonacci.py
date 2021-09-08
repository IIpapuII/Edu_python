#Recursividad con fibonacci

def fibonacci(n):
    if n==0 or n==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

#ingreso de datos del usuario
n = int(input('Ingrese un numero entero: '))

print(f'El numero fibonacci para {n} es {fibonacci(n)}')