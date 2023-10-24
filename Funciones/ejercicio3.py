"""
Ejercicio 3

Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
"""


def comparator(one, two):
    if one > two:
        return 1
    elif two > one:
        return -1
    else:
        return 0


res = comparator(7, 6)
print(res)
