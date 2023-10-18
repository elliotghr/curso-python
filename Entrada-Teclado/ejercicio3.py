"""
Ejercicio 3

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
"""

vocal = input("Ingresa una vocal en minuscula: ")
letra = input("Ingresa una letra en mayúscula: ")

letra = letra.lower()
vocal = vocal.upper()

print("El resultado es:", vocal + letra)
