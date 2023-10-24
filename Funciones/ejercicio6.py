"""
Ejercicio 6

Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""


def media(list):
    result = 0
    for item in list:
        result += item
    return result


print(media([1, 2, 3, 6]))
