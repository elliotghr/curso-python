"""
Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial."""


def factorial(number):
    number = int(input("Ingresa un número entero positivo: "))

    if number < 0:
        print("Solo acepta números positivos")
        exit()

    res = 1

    for x in range(1, number):
        res += res * x
    return res


print(factorial(7))
