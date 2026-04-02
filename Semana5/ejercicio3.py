"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    if n < 0:
        print (f"error")
    resultado = 1
    for i in range (2, n + 1):
        resultado *= i
    return resultado
    pass


def factorial_recursivo(n):
    if n < 0
        print (f"error")
    if n == 1 
        return 1
    return n * factorial_recursivo (n-1)
    pass
