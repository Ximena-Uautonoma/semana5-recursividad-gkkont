"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    suma = 0
    for i in range (1, n +1)
        suma += 1
    return suma
    pass


def suma_recursiva(n):
    if n == 0
        return 0
    return n+ suma_recursiva(n-1) 
    pass
